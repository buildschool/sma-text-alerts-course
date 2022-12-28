# import dependencies
from twilio.rest import Client
import os

# save dotenv values
config = os.environ

# define account varaibles
account = config['TWILIO_ACCOUNT_SID']
token = config['TWILIO_AUTH_TOKEN']

# define numbers
to_number = # your number
from_number = # your number from twilio

# Define twilio client
client = Client(account, token)

# def send text function
def send_text(body):
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=body
    )
    return message.sid