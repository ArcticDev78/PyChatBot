""" IMPORTS """
from random import randint
import time
import requests
import json

# Chatbot name variable (you can change it to your liking)
chatbotName = 'Chatbot'

""" FUNCTIONS """

# Send the chatbot's message with a delay of 0.2s so that it feels real


def sendBotMsg(message):
    time.sleep(0.2)
    print(f'{chatbotName}: {message}')


# Random function for returning random response from the given dictionary arrray.  # noqa
def random(array):
    arrayLength = len(array)
    rand = randint(0, arrayLength-1)
    return array[rand]


""" INTRODUCTION """

# Make the chatbot introduce itself
sendBotMsg(f'Hi! My name is {chatbotName}. What\'s your name?')
# Ask for the user's name (for the conversation)
name = input('[YOU] My name is: ')
sendBotMsg(f'Nice to meet you, {name}!')
sendBotMsg('I am a Chatbot and I can do basic things like have conversations with you.\n')  # noqa


def chatbot():
    # Take the user input through a simple input function
    userinput = input("[YOU] > ").lower()

    # Store the triggers and responses in a dictionary
    db = {
        'greetings': {
            'triggers': ['hi', 'hey', 'hello', 'heyya', 'heyya', 'sup', 'wassup', 'yo', 'ello'],  # noqa
            'responses': [f'Hello there, {name}!', f'Hi, {name}!', f'Hey, {name}!', f'What\'s up, {name}?', f'Sup, {name}!'],  # noqa
        },
        'bye': {
            'triggers': ['bye', 'cya', 'gtg', 'ttyl', 'i gtg', 'gtg bye'],
            'responses': [f'See you later, {name}!', f'Bye, {name}!', f'Cya later, {name}!'],  # noqa
        },
        'thankyou': {
            'triggers': ['ty', 'tysm', 'thanks', 'thank you'],
            'responses': ['No problem!', 'You\'re welcome!', 'Welcome!'],
        },
        'good': {
            'triggers': ['good', 'great', 'nice', 'noice', 'cool'],
            'responses': ['Awesome!', 'Great!'],
        },
        'ok': {
            'triggers': ['ok', 'okay', 'aight', 'ight', 'k', 'kk', 'alright'],
            'responses': ['Are you sure?', 'Ok.', 'Okay.'],
        },
        'yes': {
            'triggers': ['yes', 'yeah', 'ye', 'yea', 'yep', 'ya'],
            'responses': ['Fine.', 'Ok.'],
        },
        'no': {
            'triggers': ['no', 'nope', 'nah', 'na'],
            'responses': ['Why not?', 'Okay.'],
        },
        'bored': {
            'triggers': ['i\'m bored', 'im bored', 'i am bored'],
            'responses': ['Say goodbye to your boredom and chat with me!', 'Why are you bored?'],  # noqa
        },
        'nameask': {
            'triggers': ['what\'s your name?', 'whats your name?', 'what\'s your name', 'whats your name', 'whats ur name', 'whats ur name?'],  # noqa
            'responses': f'My name is {chatbotName}, the awesome chatbot! Nice to meet you, {name}',  # noqa
        },
        'noyou': {
            'triggers': ['no u', 'no you'],
            'responses': ['no u', 'no you'],
        },
        'stutterwords': {
            'triggers': ["uh", "uhm", "uh-", "uhm-", "uhh"],
            'responses': ["Hm?", "?", "What?"],
        },
        'lol': {
            'triggers': ['lol', 'lmao', 'haha', 'hahaha', 'hehe', 'xd'],
            'responses': ['Haha!', 'Funny, right?', 'xD'],
        }
    }

    if userinput in db['greetings']['triggers']:
        sendBotMsg(random(db['greetings']['responses']))

    elif userinput in db['bye']['triggers']:
        sendBotMsg(random(db['bye']['responses']))

    elif userinput in db['thankyou']['triggers']:
        sendBotMsg(random(db['thankyou']['responses']))

    elif userinput in db['good']['triggers']:
        sendBotMsg(random(db['good']['responses']))

    elif userinput in db['ok']['triggers']:
        sendBotMsg(random(db['ok']['responses']))

    elif userinput in db['yes']['triggers']:
        sendBotMsg(random(db['yes']['responses']))

    elif userinput in db['no']['triggers']:
        sendBotMsg(random(db['no']['responses']))

    elif userinput in db['bored']['triggers']:
        sendBotMsg(random(db['bored']['responses']))

    elif userinput in db['nameask']['triggers']:
        sendBotMsg(db['nameask']['responses'])

    elif userinput in db['noyou']['triggers']:
        sendBotMsg(random(db['noyou']['responses']))

    elif userinput in db['stutterwords']['triggers']:
        sendBotMsg(random(db['stutterwords']['responses']))

    elif userinput in db['lol']['triggers']:
        sendBotMsg(random(db['lol']['responses']))

    elif userinput == 'idk':
        sendBotMsg('You don\'t know?')

    elif userinput == 'why':
        sendBotMsg('I don\'t know either.')

    elif userinput == 'ok boomer':
        sendBotMsg("Sure. Who is your best friend?")

    elif userinput == 'hmm':
        sendBotMsg("Hmmm.")

    elif userinput == 'sad':
        sendBotMsg("No, never be sad!")

    elif userinput == 'fine':
        sendBotMsg('Fine!')

    elif userinput == 'ping':
        sendBotMsg("Pong!")

    elif userinput == 'are you here':
        sendBotMsg('Yes! I am here!')

    elif userinput == 'tell me a joke':
        data = requests.get(r"https://official-joke-api.appspot.com/random_joke")  # noqa
        joke = json.loads(data.text)
        sendBotMsg(f'{joke["setup"]}\n         {joke["punchline"]}')

    elif userinput == 'so what':
        sendBotMsg("Idk")

    else:
        sendBotMsg("I'm not sure I understand.")


# Use an infinite loop to keep the conversation going
# Using an infinite loop is probably a bad idea
i = 0
while i <= 10:
    chatbot()
