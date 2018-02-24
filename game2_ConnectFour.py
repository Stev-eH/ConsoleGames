import os
import random

def clear():
    command = ''
    if os.name == 'nt':
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

def draw(state,pl):
    clear()
    print('\nConnect Four\n')
    screen = '|'
    player = ''
    for y in range(6):
        for x in range(7):
            if state[y][x] == 0:
                screen += '.|'
            elif state[y][x] == 1:
                screen += 'X|'
            elif state[y][x] == 2:
                screen += 'O|'
            else:
                screen += '-|'
        print(screen)
        screen = '|'
    print('|1|2|3|4|5|6|7|\n')

def solo_or_vs(x):
    if x == '2':
        return 1
    else:
        return 0
    
def player_Turn(state,pl):
    choice = 0
    turn = True
    i = 0
    icon = ''
    if pl == 1:
        icon = 'X'
    else:
        icon = 'O'
    print('Turn of ' + icon+'\n')
        
    while turn == True:
        try:
            choice = int(input('Select a row: '))-1
            if choice >= 0 and choice <= 6:
                for y in range(7):
                    i = 6 - y
                    if i == 0:
                        print('Stack is full')
                    elif state[i-1][choice] == 0:
                        state[i-1][choice] = pl
                        turn = False
                        return state
            else:
                print('Select a number between 1 and 7')
        except ValueError:
            print('Dude!')

def dumb_AI(state):
    choice = random.randint(0,6)
    turn = True
    i = 0
    while turn == True:
        for y in range(7):
            i = 6 - y
            if i == 0:
                choice = random.randint(0,6)
            elif state[i-1][choice] == 0:
                state[i-1][choice] = 2
                return state

def board_Full(state):
    for i in range(len(state)):
        if state[i] == 0:
            return False
    return True

def game_Win(state,pl):
    #Horizontal
    for y in range(6):
        for x in range(4):
            if state[y][x:x+4] == [pl,pl,pl,pl]:
                state[y][x:x+4] = [3,3,3,3]
                return state
    #Vertikal
    i = 0
    for x in range(7):
        for y in range(4):
            i = 5 - y
            if state[i][x] == pl:
                if state[i-1][x] == pl:
                    if state[i-2][x] == pl:
                        if state[i-3][x] == pl:
                            state[i][x] = 3
                            state[i-1][x] = 3
                            state[i-2][x] = 3
                            state[i-3][x] = 3
                            return state

    #Diagonal UL/OR
    j = 0
    for y in range(3):
        for x in range(4):
            j = 5 - y
            if state[j][x] == pl:
                if state[j-1][x+1] == pl:
                    if state[j-2][x+2] == pl:
                        if state[j-3][x+3] == pl:
                            state[j][x] = 3
                            state[j-1][x+1] = 3
                            state[j-2][x+2] = 3
                            state[j-3][x+3] = 3
                            return state

    #Diagonal OL/UR
    k = 0
    l = 0
    for y in range(3):
        for x in range(4):
            k = 5 - y
            l = 3 + x
            if state[k][l] == pl:
                if state[k-1][l-1] == pl:
                    if state[k-2][l-2] == pl:
                        if state[k-3][l-3] == pl:
                            return state
            
                        
    return state

def play_Again():
    replay = input("Play again? (y/n) ")
    if 'y' in replay:
        game()
    else:
        print("Goodbye!")

def game():
    state = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    
    player = random.randint(1,2)
    game = True
    AI = 0
    draw(state,player)
    end = False
    AI = solo_or_vs(input("How many Players? (1 or 2): "))
    
#####################Spielablauf#########################################
    
    while game == True:
        
        draw(state,player)
        
        if player == 1:
            state = player_Turn(state,player)
            state = game_Win(state,player)
            player = 2
            
        elif player == 2:
            if AI != 0:
                state = player_Turn(state,player)
                state = game_Win(state,player)
            else:
                state = dumb_AI(state)
                state = game_Win(state,player)
            player = 1
            
        if board_Full(state[0]) == True:
            draw(state,player)
            print("\nIt's a draw!")
            game = False
        n = 0
        for x in range(7):
            for y in range(6):
                if state[y][x] == 3:
                    game = False
                    end = True

    if end == True:
        draw(state,player)
        icon = ''
        if player == 1:
            icon = 'O'
        else:
            icon = 'X'
        print("\n" + icon + " won!\n")
        play_Again()
            
######################################################################

game()

