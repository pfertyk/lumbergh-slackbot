from slackclient import SlackClient
import time
import os

token = os.environ.get('SLACKBOT_LUMBERGH_TOKEN')

sc = SlackClient(token)

link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'

if sc.rtm_connect():
    while True:
        events = sc.rtm_read()
        for event in events:
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']
                if 'that would be great' in text.lower() and link not in text:
                    sc.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=link,
                        as_user='true:'
                    )
        time.sleep(1)
else:
    print('Connection failed, invalid token?')
