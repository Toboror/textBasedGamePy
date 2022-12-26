import random

class Casino:

    def playBlackjack(self):
        

    def playRoulette(self):

    def playDice(self):



# Standard Yes/No answer
def yesNo():
    print('1. Yes \n'
          '2. No')


# Standard Yes/No with added third option
def hookerInteraction():
    print('1. Yes \n' +
          '2. No \n' +
          '3. Tell her she stinks.')


# Standard Yes/No with added third option
def oldManInteraction():
    print('1. Yes \n' +
          '2. No \n' +
          '3. Kick the old man and steal his stuff.')


# Stranger tell name
def strangerTellName():
    print('1. My name is ' + name + '\n' +
        '2. My name is Michael\n' +
        '3. My name is Fido')


# Casino choose game
def casinoChooseGame():
    print('1. Blackjack \n' +
          '2. Roulette \n' +
          '3. Dice')


userHealth = 10
while userHealth > -1:

    # Choose name
    while True:
        while True:
            name = input("What is your name?" + "\n")
            print('Is your name ' + name + "?")
            answer = input("y for yes, n for no")
            if answer == "y":
                break

    # Check gold amount
    userGold = 100
    print('Do you want to check how much gold you have?')
    answerGold = input('Yes or no?' + "\n")

    if answerGold == 'y':
        print('Your amount of gold is: ' + str(userGold))

    print('Sure. Let us continue.')

    # Secret stash
    print('A random stranger approaches you. The stranger want to know your name. \n'
          'What will you tell the stranger?')
    answerTellName = input(strangerTellName())
    fakeName = ''
    if answerTellName == '1':
        print('Nice to meet you, ' + name)
    elif answerTellName == '2':
        fakeName = 'Michael'
        print('Nice to meet you, ' + fakeName)
    else:
        fakeName = 'Fido'
        print('Nice to meet you, ' + fakeName)
    print('The stranger asks if you would like to buy his secret stash. It costs 100 gold.')
    answerSecretStash = input(yesNo())
    secretStash = 0
    if answerSecretStash == '1':
        print('He says have a good day.')
        userGold -= 100
        secretStash += 1
    elif answerSecretStash == '2':
        print('Sure thing. You did not buy the secret stash.')

    if secretStash == 1:
        print('Do you want to open the secret stash?')
        answerOpenSS = input(yesNo())
        if answerOpenSS == '1':
            print('You decide to open the secret stash. \n'
                  'You receive 200 gold.')
            userGold += 200
        elif answerOpenSS == '2':
            print('Fine. It shall remain a secret.')

    # Hooker encounter
    print('You meet a hooker on the street. Do you want to do the smash?')
    hookerInteraction()
    answerHooker = input('')
    std = 0
    userHappiness = 25
    hookerRelation = 100
    if answerHooker == '1':
        print('You got some nice smash. And you got STD`s. \n'
              'This has slightly reduced your health, \n'
              'but you are feeling a little happier.')
        std += 1
        userHealth -= 2
        userHappiness += 5
    elif answerHooker == '2':
        print('You did not get some nice smash. Sad times.')
    elif answerHooker == '3':
        print('You told the hooker that she stinks.')
        hookerRelation -= 10

    if userHealth < 10:
        print('You are feeling a little subpar')

    # Funny mushroom
    print('You stumble upon a funny looking mushroom. Do you want to eat it?')
    yesNo()
    answerFunnyShroom = input('')
    if answerFunnyShroom == '1':
        print('You are a fucking idiot.')
        userHealth -= 5
    elif answerFunnyShroom == '2':
        print('You are a smart looking fella. Good on you. \n'
              'Do you want to pick it up instead?')
        yesNo()
        answerFunnyShroom2 = input('')
        funnyShroom = 0
        if answerFunnyShroom2 == '1':
            print('You decide to pick up the funny looking mushroom.')
            funnyShroom += 1
        elif answerFunnyShroom2 == '2':
            print('That is alright. At least you did not eat it.')

    # Health remedy
    oldManRelation = 100
    if userHealth <= 4 and userGold >= 150:
        print('You are feeling kind of terrible. \n'
              ' Do you want to go looking for a health remedy?')
        yesNo()
        answerSickness = input('')
        if answerSickness == '1':
            print('You found an old looking man selling some old remedies. \n'
                  'Do you want to buy one for 150 gold?')
            oldManInteraction()
            oldRemedy = 0
            answerSickness2 = input('')
            if answerSickness2 == '1':
                print('You bought the old remedy. Do you want to drink it?')
                userGold -= 150
                oldRemedy += 1
                yesNo()
                answerSickness2 = input('')
                if answerSickness2 == '1':
                    print('You decided to drink the remedy. You feel better.')
                    oldRemedy -= 1
                    userHealth += 3
                elif answerSickness2 == '2':
                    print('You decide to keep the remedy for later.')
            elif answerSickness2 == '2':
                print('You did not buy the old remedy.')
        elif answerSickness == '2':
            print('You decide to not go looking for a remedy for your health.')
        elif answerSickness == '3':
            print('You decided to kick the poor old man. Shame on you,\n '
                  'but you you got an old remedy.')
            oldManRelation -= 40
            userHappiness -= 5
            print('Do you want to spit on the old man while he lies helplessly on the ground?')
            yesNo()
            oldManSpit = input('')
            if oldManSpit == '1':
                print('You decide to spit the old man in addition to already having kicked him.')
                oldManRelation -= 20
                userHappiness -= 10
                # Old man relation reduced to 80
                # User happiness reduced by -15
            elif oldManSpit == '2':
                print('You decide to be a decent human being and not spit in the old man, \n'
                      'even though you already kicked him.')

    # Random demon encounter
    randomEncounter = random.randint(0, 3)
    demonHealth = 1000
    if randomEncounter == 0:
        print('You met an evil demon. \n'
              'What do you want to do?')
        print('1. Attack the demon \n'
              '2. Run like a kitty cat')
        answerDemonEnc = input('')
        if answerDemonEnc == '1' and userHealth < 100:
            print('You bitch slap the demon while the demon disembowels you. \n'
                  'You proceed to die.')
            demonHealth -= 1
            userHealth -= 99
        elif answerDemonEnc == '1' and userHealth >= 100:
            print('You are almost killed by the demon, but you manage to run away.')
            userHealth -= 99
        elif answerDemonEnc == '2':
            print('You decide to live another day.')

    # Event from low happiness
    if userHappiness == 15:
        print('You proceed to scream because of your dissatisfaction. \n'
              'This has attracted wild snakes which attack you.')
        userHealth -= 40

    # Casino Arc
    answerCasino = input(print('You stumble upon a casino. Do you wish to go in?'))
    yesNo()
    if answerCasino == '1':
        answerCasinoGame = input(print('You decide to enter the casino. \n'
                                       'When you entered the casino you see alot of games that you can play. \n'
                                       'Do you want to play Blackjack, Roulette or Dice?'))
        casinoChooseGame()
        # Blackjack
        if answerCasinoGame == '1':
            print('You decide to play Blackjack.')
            Casino.playBlackjack()
        # Roulette
        elif answerCasinoGame == '2':
            print('You decide to play Roulette.')
        # Dice
        elif answerCasinoGame == '3':
            print('You decide to play Dice.')
    elif answerCasino == '2':
        print('You carry on.')

