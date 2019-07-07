# import all the libraries we will be using

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)

# Main method
@app.route('/sms', methods=['POST'])
def sms_reply():
    # twilio response object
    resp = MessagingResponse()

    # Get text in message sent
    body = request.form['Body']

    # Case Statement showing all the reponse options
    if body == 'HELP':
        resp.message("Thank you for your response! We are going to find some help for you!")
    elif body == 'SUPPORT':
        resp.message("Support Message here")
    else:
        resp.message("\n Welcome to DeliverAid! \nThank you, "
                     "\"can you tell us where you are now so we can find you!\"\n")

    return str(resp)


if __name__ == '__main__':
    app.run()
