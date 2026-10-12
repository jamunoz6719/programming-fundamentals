import random

# Variables del juego
life1 = 5
life2 = 5
shift = 1
winner = False
counter = 0

player1 = input('Type the name of the player 1: ')
player2 = input('Type the name of the player 2: ')

print('The player ' + player1 + ' Start')
print('Game: two players, five lives each')

while life1 > 0 and life2 > 0 and not winner:
    if shift == 1:
        print('Turn of ' + player1)
    else:
        print('Turn of ' + player2)

    input('Press Enter to roll')

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    add = dice1 + dice2
    counter += 1

    print('Dice 1:', dice1)
    print('Dice 2:', dice2)
    print('Sum:', add)

    if dice1 == 1 and dice2 == 1:
        winner = True
        if shift == 1:
            print(player1 + ' WON with double ones!')
        else:
            print(player2 + ' WON with double ones!')
    else:
        if add % 2 == 0:
            print('Even sum. Lives stay the same')
        else:
            if shift == 1:
                life1 -= 1
                print('Lives of ' + player1 + ':', life1)
            else:
                life2 -= 1
                print('Lives of ' + player2 + ':', life2)

        if life1 == 0:
            print(player2 + ' WON! ' + player1 + ' ran out of lives.')
            winner = True
        elif life2 == 0:
            print(player1 + ' WON! ' + player2 + ' ran out of lives.')
            winner = True

    if not winner:
        if shift == 1:
            shift = 2
        else:
            shift = 1

print('Total rolls:', counter)
print('Final lives - ' + player1 + ':', life1)
print('Final lives - ' + player2 + ':', life2)
