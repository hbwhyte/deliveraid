from twilio.rest import Client

account_sid = 'your account id here'
auth_token = 'your token here'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="Join Earth's mightiest heroes. Like Charles and Evie!.",
        from_='+441522246102',
        to='your number here'
    )

print(message.sid)
