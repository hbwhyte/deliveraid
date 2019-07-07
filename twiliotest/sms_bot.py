from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():

    resp = MessagingResponse()
    body = request.form['Body']
    if "HELP" in body:
        resp.message("Thank you for your response! We are going to find some help for you!")
    elif "SUPPORT" in body:
        resp.message("Support Message here")
    else:
        resp.message("\n Welcome to DeliverAid! These are the commands you may use: \nHELP "
                     "\"get help from one of our partners\" \nSUPPORT \"support request\"\nOTHER \"place\""
                     "\nSOME_KEYWORD \"some custom request\"\n")

    return str(resp)


if __name__ == '__main__':
    app.run()



