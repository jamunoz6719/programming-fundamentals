from random import randint

#Inizialize
odd = 0
pair = 0
equal = 0   
lives = 5

playername = input('Type the name of player: ')
totalroll = int(input('Please Type the number of rolls: '))


for i in range(totalroll):
    if lives > 0:
        message = input('Press enter for start')
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        print('Dice 1 :', dice1)
        print('Dice 2 :', dice2)
        add = dice1 + dice2
        print('The summ of the dices is:', add)
        if add % 2 == 0:
            pair = pair + 1
            if dice1 == dice2:
               equal = equal + 1 
            if lives == 5:
                print('The lives are completed')
            else:
                lives = lives + 1                
        else:
            odd = odd + 1
            lives = lives - 1
            if lives == 0:
                print('YOU LOST ALL THE LIVES')
        print(f'the lives disponible: {lives}')
    


print(f'The player {playername} terminated the game with {lives} lives ')                
print('The total of pair is:', pair)
print('The total of odd is:', odd)
print('The total of equal is:', equal)
        
    