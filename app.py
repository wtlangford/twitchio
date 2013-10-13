from twilio.rest import TwilioRestClient
import yaml
import json
import requests
import database
#import client
from pprint import pprint as pp

config = yaml.load(open('config.yaml'))
account_sid = config['account_sid']
auth_token = config['auth_token']
client = TwilioRestClient(account_sid, auth_token)
listChannels = database.getChannelsToCheck()

for channel in listChannels :
  r = requests.get("https://api.twitch.tv/kraken/streams/"+channel)
  #pp(r.json()['stream'])
  if r.json()['stream'] == None :
    database.channelDidStopStreaming(channel)
  else :
    database.channelDidStartStreaming(channel)
  if database.isChannelNewlyStreaming(channel) :
    listNumbers = database.numbersForChannel(channel)
    for number in listNumbers :
      message = client.sms.messages.create(body=channel+" is online.", to="+1"+number, from_="17325202749")
      print message.sid
