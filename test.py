from twilio.rest import TwilioRestClient
import yaml
import json
import requests
from pprint import pprint as pp

username = raw_input("Username: ")
phonenumber = raw_input("Number: +1")
requestString = "https://api.twitch.tv/kraken/channels/"+username+"/follows"
r = requests.get(requestString)
config = yaml.load(open('config.yaml'))
account_sid = config['account_sid']
auth_token = config['auth_token']
client = TwilioRestClient(account_sid, auth_token)
#list of followers
followers = [l['user']['name'] for l in r.json()['follows']]
addUser(phonenumber, followers)
#message = client.sms.messages.create(body="yay text message", to="+19084216532", from_="+17325202749")
#print message.sid
