# Snake, Water and Gun game
import random as rr

def game(player, comp):

    if player == comp:
        print('Draw between player and computer\n')
    elif (player == 0 and comp == 2) or (player == 2 and comp == 1) or (player == 1 and comp == 0):
        print("Player loses the game\n")
    else:
        print("Player wins the game\n")
    
print('''Choice 
* Enter 0 for Snake * 
* Enter 1 for Water * 
* Enter 2 for Gun   * ''')
try:
    player = int(input("Enter player choice (0, 1, or 2): "))
    if player < 0 or player > 2 :
            raise  ValueError("Value should be an 'Integer' and only '0 , 1 or 2' ")

    comp = rr.randint(0,2)
    # print(comp)

    print(f'\nPlayer chose {player}')
    print(f'Computer chose {comp}\n')

    game(player , comp)
except ValueError as e:
    print(e)
