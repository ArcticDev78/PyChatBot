from random import randint

i = 0

while i <= 10:

    # for i in range():

    userinput = input("> ").lower()

    greetingtriggers = [
        'hi', 'hey', 'hello', 'heyya', 'hewwo', 'sup', 'wassup'
    ]

    if userinput in greetingtriggers:
        replies = ['Hello there!', 'Hi!', 'Hey!', 'What\'s up?', 'Sup!']
        result = replies[randint(0, 4)]
        print(result)

    byetriggers = ['bye', 'cya', 'gtg', 'ttyl']

    if userinput in byetriggers:
        replies = ['See you later!', 'Bye!', 'Cya!']
        result = replies[randint(0, 2)]
        print(result)

    thankyou = ['np', 'you\'re welcome', 'welcome', 'ty', 'tysm']

    if userinput in thankyou:
        replies = ['No problem!', 'You\'re welcome!', 'Welcome!']
        result = replies[randint(0, 2)]
        print(result)

    goodtriggers = ['good', 'great', 'nice', 'noice', 'cool']

    if userinput in goodtriggers:
        replies = ['Awesome!', 'Great!']
        result = replies[randint(0, 1)]
        print(result)

    elif userinput == 'ok':
        replies = ['Are you sure?', 'Ok.']
        result = replies[randint(0, 1)]
        print(result)

    elif userinput == 'yes':
        replies = ['Fine.', 'Ok.']
        result = replies[randint(0, 1)]
        print(result)

    elif userinput == 'no':
        replies = ['Why not?', 'Don\'t say that again!']
        result = replies[randint(0, 1)]
        print(result)

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

    yeahtriggers = ['yeah', 'yea', 'ya']

    if userinput in yeahtriggers:
        print('Ok!')

    bored = ['i\'m bored', 'im bored']

    if userinput in bored:
        print("Say goodbye to your boredom and chat with me!")

    nameask = [
        'what\'s your name?', 'whats your name?', 'what\'s your name',
        'whats your name'
    ]

    if userinput in nameask:
        print(
            "My name is Infinity, the awesome chatbot!")

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

    noyou = ['no you', 'no u']

    if userinput in noyou:
        replies = ['no u', 'no you']
        result = replies[randint(0, 1)]
        print(result)

    stutterwords = ["uh", "uhm", "uh-", "uhm-", "uhh"]

    if userinput in stutterwords:
        replies = ["Hm?", "?", "What?"]
        result = replies[randint(0, 2)]
        print(result)

    elif userinput == 'so what':
        print("Idk")

    # else:
        # print("I'm not sure I understand")
