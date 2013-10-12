from twilio.rest import TwilioRestClient
import yaml
import json
import requests

r = requests.get("https://api.twitch.tv/kraken/channels/ace6598/follows")
print(r.json()['follows'])
config = yaml.load(open('config.yaml'))
account_sid = config['account_sid']
auth_token = config['auth_token']
client = TwilioRestClient(account_sid, auth_token)
#message = client.sms.messages.create(body="TEST", to="+17326681916", from_="+17325202749")
#print message.sid
