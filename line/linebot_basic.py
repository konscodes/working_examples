from os import environ
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
import schedule
import time

# Set up Line bot credentials
line_bot_api = LineBotApi(str(environ.get('LINE_CHANNEL_ACCESS_TOKEN')))
handler = WebhookHandler(str(environ.get('LINE_CHANNEL_SECRET')))

# Set up message to be sent
message = TextSendMessage(text='Hello, this is a weekly reminder!')

# Define function to send message
def send_message(group_id, message):
    # Send the message to the group
    line_bot_api.push_message(group_id, message)

# Schedule the task to run every week
schedule.every().minute.do(
    lambda: send_message('Cd8838ffe33ac87f0595ac2be8ce6579f', message))

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)