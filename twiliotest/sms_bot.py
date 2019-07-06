from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():

    resp = MessagingResponse()
    body = request.orm['Body']
    if "HELP" in body:
        resp.message("Thank you for your response! We are going to find some help for you!")
    elif "SUPPORT" in body:
        resp.message("Support Message here")
    else:
        resp.message("Welcome to DeliverAid! To use this service text HELP and we'll get back to you")

    return str(resp)

    if __name__ == '__main__':
        app.run()