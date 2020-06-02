#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Preset values:
accountSID = 'SID HERE'
authToken = 'AUTHTOKEN HERE'
myNumber = 'NUMBER HERE'
twilioNumber = 'NUMBER HERE'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

