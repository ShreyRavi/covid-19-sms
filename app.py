#app.py
#main Flask app for COVID-19 SMS Update

#imports
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse
from get_data import reply

#Flask app initialization
app = Flask(__name__)

#homepage route
@app.route("/")
def homepage():
    return render_template("index.html")

#sms route
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """dynamic COVID-19 SMS Update response to incoming text"""
    body = request.values.get('Body', None).strip()
    resp = MessagingResponse()
    resp.message(reply(body))
    return str(resp)

#call route
@app.route("/voice", methods=['GET', 'POST'])
def incoming_call():
    """static COVID-19 SMS Update voice response to incoming call"""
    resp = VoiceResponse()
    resp.say("Thanks for Calling CoronaUpdate Service. Please text 231 774 2545 with a zipcode, a City, State Code (such as Chicago comma IL), or a state (such as IL) to get the latest COVID 19 updates for that area. Thanks, and have a great day!", voice='alice')
    return str(resp)

#run Flask app
if __name__ == "__main__":
    app.run()