from flask import Flask, request, redirect
import twilio.twiml
import client

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello_monkey():
  print "i got something"
  from_number = request.values.get('From',None)
  resp = twilio.twiml.Response()
  resp.message(message)
  return str(resp)

if __name__== "__main__":
  app.run(debug=True)
