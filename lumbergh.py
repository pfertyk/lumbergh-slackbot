from slackclient import SlackClient
import os
from flask import Flask, request, Response


app = Flask(__name__)
link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'

client_token = os.environ.get('SLACKBOT_LUMBERGH_TOKEN')
webhook_token = os.environ.get('SLACKBOT_WEBHOOK_TOKEN')

sc = SlackClient(client_token)


@app.route('/lumbergh', methods=['POST'])
def inbound():
    print('incoming')
    if request.form.get('token') == webhook_token:
        print('verified')
        channel = request.form.get('channel_name')
        text = request.form.get('channel_name')
        if 'that would be great' in text.lower() and link not in text:
            sc.api_call(
                'chat.postMessage',
                channel=channel,
                text=link,
                as_user='true:'
            )
    return Response(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
