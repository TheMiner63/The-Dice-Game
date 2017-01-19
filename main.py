#Copyright 2017 Chris Boddy
#This program is a demo, created for use in the classroom.
#Only use with explicit permission from the author.

import random
scoreComments = ['Better luck next time!','Could be better!','Well done!','Very lucky!']

def main():
    print('Copyright 2017 Chris Boddy\nWelcome to the dice game!')
    playGame = False
    playAgain = True
    while True:
        start = input('Start the game? Y/N\n').lower().strip()
        if (start == 'y' or start == 'yes'):
            playGame = True
        elif (start == 'n' or start == 'no'):
            playGame = False
            break
        else:
            print('Sorry, didn\'t get that...')
        while playGame:
            d1, d2 = random.randint(1,6), random.randint(1,6)
            print('Rolling...\n{} {}'.format(d1,d2))
            score = d1 + d2
            if (d1 == d2):
                if (d1 == 6):
                    score = 0
                else:
                    score = score * 2
            print('Your overall score: {}'.format(score))
            print(scoreComments[round(score/3)])
            while True:
                restart = input('Play again? Y/N\n').lower().strip()
                if (restart == 'y' or restart == 'yes'):
                    playAgain = True
                    break
                elif (restart == 'n' or restart == 'no'):
                    playAgain = False
                    break
                else:
                    print('Sorry, didn\'t get that...')
            if not playAgain:
                break
        if not playAgain:
            break
    print('Thanks for playing!')
    return

if (__name__ == '__main__'):
    main()
