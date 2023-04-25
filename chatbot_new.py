""" IMPORTS """
from random import randint
import time

# Chatbot name variable (you can change it to your liking)
chatbotName = 'Chatbot'

""" FUNCTIONS """

# Send the chatbot's message with a delay of 0.2s so that it feels real


def sendBotMsg(message):
    time.sleep(0.2)
    print(message)


# Random function for returning random response from the given dictionary arrray.  # noqa
def random(array):
    arrayLength = len(array)
    rand = randint(0, arrayLength-1)
    return array[rand]


""" INTRODUCTION """

# Make the chatbot introduce itself
print(f'{chatbotName}: Hi! My name is {chatbotName}. What\'s your name?')
# Ask for the user's name (for the conversation)
name = input('[YOU] My name is: ')
sendBotMsg(f'{chatbotName}: Nice to meet you, {name}!')
sendBotMsg(f'{chatbotName}: I am a Chatbot and I can do basic things like have conversations with you.\n')  # noqa


def chatbot():
    # Take the user input through a simple input function
    userinput = input("[YOU] > ").lower()

    # Store the triggers and responses in a dictionary
    db = {
        'greetings': {
            'triggers': ['hi', 'hey', 'hello', 'heyya', 'heyya', 'sup', 'wassup', 'yo', 'ello'],  # noqa
            'responses': ['Hello there!', 'Hi!', 'Hey!', 'What\'s up?', 'Sup!'],  # noqa
        },
        'bye': {
            'triggers': ['bye', 'cya', 'gtg', 'ttyl', 'i gtg', 'gtg bye'],
            'responses': ['See you later!', 'Bye!', 'Cya!'],
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
            'triggers': ['yes', 'yeah', 'ye', 'yea', 'yep'],
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
            'responses': f'My name is {chatbotName}, the awesome chatbot!',
        },
        'noyou': {
            'triggers': ['no u', 'no you'],
            'responses': ['no u', 'no you'],
        },
        'stutterwords': {
            'triggers': ["uh", "uhm", "uh-", "uhm-", "uhh"],
            'responses': ["Hm?", "?", "What?"],
        }
    }

    if userinput in db['greetings']['triggers']:
        # print(random(db['noyou']['responses']))
        # result = db['greetings']['responses'][randint(0, 4)]
        sendBotMsg(random(db['greetings']['responses']))

    elif userinput in db['bye']['triggers']:
        # result = db['bye']['responses'][randint(0, 2)]
        sendBotMsg(random(db['bye']['responses']))

    elif userinput in db['thankyou']['triggers']:
        # result = db['bye']['responses'][randint(0, 2)]
        sendBotMsg(random(db['thankyou']['responses']))

    elif userinput in db['good']['triggers']:
        # result = db['good']['responses'][randint(0, 1)]
        sendBotMsg(random(db['good']['responses']))

    elif userinput in db['ok']['triggers']:
        # result = db['ok']['responses'][randint(0, 1)]
        sendBotMsg(random(db['ok']['responses']))

    elif userinput in db['yes']['triggers']:
        # result = db['yes']['responses'][randint(0, 1)]
        sendBotMsg(random(db['yes']['responses']))

    elif userinput in db['no']['triggers']:
        # result = db['no']['responses'][randint(0, 1)]
        sendBotMsg(random(db['no']['responses']))

    elif userinput in db['bored']['triggers']:
        # result = db['bored']['responses'][randint(0, 1)]
        sendBotMsg(random(db['bored']['responses']))

    elif userinput in db['nameask']['triggers']:
        sendBotMsg(db['nameask']['responses'])

    elif userinput in db['noyou']['triggers']:
        # result = db['noyou']['responses'][randint(0, 1)]
        sendBotMsg(random(db['noyou']['responses']))

    elif userinput in db['stutterwords']['triggers']:
        # result = db['stutterwords']['responses'][randint(0, 2)]
        sendBotMsg(random(db['stutterwords']['responses']))

    elif userinput == 'idk':
        print('You don\'t know?')

    elif userinput == 'why':
        print('I don\'t know either.')

    elif userinput == 'ok boomer':
        print("Sure. Who is your best friend?")

    elif userinput == 'lol':
        replies = ['Haha!', 'Funny, right?', 'xD']
        result = replies[randint(0, 2)]
        print(result)

    elif userinput == 'hmm':
        print("Hmmm.")

    elif userinput == 'sad':
        print("No, never be sad!")

    elif userinput == 'fine':
        print('Fine!')

    elif userinput == 'ping':
        print("Pong!")

    elif userinput == 'are you here':
        print('Yes! I am here!')

    elif userinput == 'tell me a joke':
        replies = ['Today at the bank, an old lady asked me to help check her balance. So I pushed her over.',  # noqa
                   'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.',  # noqa
                   'Why is Peter Pan always flying? He neverlands.',
                   'What do you call a guy with a rubber toe? Roberto.',
                   'What did the pirate say when he turned 80 years old? Aye matey.'  # noqa
                   ]
        result = replies[randint(0, 4)]
        print(result)

    elif userinput == 'so what':
        print("Idk")

    else:
        print("I'm not sure I understand.")


# Use an infinite loop to keep the conversation going
# Using an infinite loop is probably a bad idea
i = 0
while i <= 10:
    chatbot()
