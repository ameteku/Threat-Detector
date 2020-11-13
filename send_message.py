# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


account_sid ='ACc6c11fe389e624214593df0a87a724a1'
auth_token = 'ee995147d52a98ae40e3f6ec4dbc9dbd'
client = Client(account_sid, auth_token)

f= open("foundorNot.txt", 'r')
names = f.readlines()
animal= "bottle\n"


if(animal in names):
    message = client.messages \
                    .create(
                        body="We saw a dog in you apt.",
                        from_='+12058517392',
                        to='+17404058840'
                    )


print(message.sid)
