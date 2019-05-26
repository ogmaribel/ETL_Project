from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient

import os

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = '25151c2cc3883c82d7936ea041347e40'
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = 'xoxb-632224482339-644555738581-TFspfnvugw4GhFJN7ZiYO2md'
slack_client = SlackClient(slack_bot_token)

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]

    #Chatbot
    chatbot = ChatBot("Expensiest")
    #conversation = training
    #trainer = ListTrainer(chatbot)
    #trainer.train(conversation)

    # If the incoming message contains "hi", then respond with a "Hello" message
    resultado = chatbot.get_response(message.get('text'))
    print("BOT: " +str(resultado))
    if message.get("subtype") is None:
        channel = message["channel"]
        #message = "Hello <@%s>! :tada:" % message["user"]
        message = f"{str(resultado)} <@%s>! :tada:" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=message)

        


# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.api_call("chat.postMessage", channel=channel, text=text)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=8080)