from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():

    resp = MessagingResponse()

    resp.message("Thank you for your response! We are going to find some help for you!")

    return str(resp)

if __name__ == '__main__':
    app.run()