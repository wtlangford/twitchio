import MySQLdb
import yaml

cfg = yaml.load(open('config.yaml'))

def addUser(phoneNumber,channels) :
	db = MySQLdb.connect(user=cfg['sql_username'],passwd=cfg['sql_password'],db=cfg['dbname'])
	c = db.cursor()
	c.executemany("""INSERT INTO users (user,channel) VALUES (%s, %s)""",[(phoneNumber,ch) for ch in channels])
	db.commit()

def numbersForChannel(channel) :
	db = MySQLdb.connect(user=cfg['sql_username'],passwd=cfg['sql_password'],db=cfg['dbname'])
	c = db.cursor()
	c.execute("""SELECT user FROM users WHERE channel = %s""",channel)
	return [res[0] for res in c.fetchall()]

def getChannelsToCheck() :
	db = MySQLdb.connect(user=cfg['sql_username'],passwd=cfg['sql_password'],db=cfg['dbname'])
	c = db.cursor()
	c.execute("""SELECT DISTINCT channel FROM users""")
	return [res[0] for res in c.fetchall()]
