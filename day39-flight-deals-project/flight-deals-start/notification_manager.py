from twilio.rest import Client

ACCOUNT_SID = TWILIO_ACCOUNT_SID
AUTH_TOKEN = TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = "+15419098143"
TWILIO_VERIFIED_NUMBER = "+233543166742"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
    def send_notification(self, message_to_send):
        message = self.client.messages.create(
            body=message_to_send,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message)
