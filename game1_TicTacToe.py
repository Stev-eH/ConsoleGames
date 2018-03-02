import os
from random import randint 

def clear(): #clear() leert die Konsolenansicht
    command = ''
    if os.name == 'nt':
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)

def Game_WinCheck(p,state): #überprüft nach einem Spielerzug ob der jeweilige Spieler gewonnen hat
            res = ''
            if state[0] == [p,p,p] or state[1] == [p,p,p] or state[2] == [p,p,p]:
               	game = False 
            elif(((state[0][0] == p and state[1][0] == p) and state[2][0] == p) or ((state[0][1] == p and state[1][1] == p) and state[1][2] == p) or ((state[2][0] == p and state[2][1] == p) and state[2][2] == p)):
                game = False
            elif(((state[0][0] == p and state[1][1] == p) and state[2][2] == p) or ((state[2][0] == p and state[1][1] == p) and state[0][2] == p)):
                game = False
            if game == False:
                if p == 1:
                    res = 'You win!'
                else:
                    res = 'You lose!'
            return res #gibt einen leeren String aus falls niemand gewonnen hat

def Draw_Screen(state): #überprüft den aktuellen Zustand des Spielfelds und gibt ihn grafisch aus
            clear()  #die clear() Funktion wurde hier mit eingebettet, damit die Konsole jedes mal geleert wird bevor das neue, aktuelle Spielfeld angezeigt wird
            print('\ntictactoe\n')
            screen = ''
            for y in range(3):
                for x in range(3):
                    if state[y][x] == 0: 
                        screen += '. '
                    elif state[y][x] == 1:
                        screen += 'X '
                    else:
                        screen += 'O '
                print(screen) #die Reihe wird nach der iteration von x ausgeben, damit für die nächste iteration von y eine neue Zeile "zur verfügung steht"
                screen = '' 

def player_Move(pl,turn,state): #wartet auf die Eingabe einer Zahl von 1-9, wenn das entsprechende Feld leer ist (state[?][?] == 0) wird dem Feld ein neuer Wert, je nach Speiler ,1 für X oder 2 für O zugewiesen)
                                #im Anschluss wird state wieder ausgegeben
    while(turn == True):
        print('') 
        print('______\n1|2|3|\n4|5|6|\n7|8|9|\n------')
        print('')
        choice = input('Choose a Field (1 = Top Left 9 = Bottom Right): ')

        if choice == '1' and state[0][0] == 0:    
            state[0][0] = pl                    
            turn = False
            return state
        elif choice == '2' and state[0][1] == 0:  
            state[0][1] = pl
            turn = False
            return state
        elif choice == '3' and state[0][2] == 0:  
            state[0][2] = pl   
            turn = False
            return state
        elif choice == '4' and state[1][0] == 0:
            state[1][0] = pl
            turn = False
            return state
        elif choice == '5' and state[1][1] == 0:
            state[1][1] = pl
            turn = False
            return state
        elif choice == '6' and state[1][2] == 0:
            state[1][2] = pl
            turn = False
            return state
        elif choice == '7' and state[2][0] == 0:  
            state[2][0] = pl
            turn = False
            return state
        elif choice == '8' and state[2][1] == 0:
            state[2][1] = pl
            turn = False
            return state
        elif choice == '9' and state[2][2] == 0:  
            state[2][2] = pl
            turn = False
            return state
        else:
            print('Invalid move!')

def mock_AI(state): #Computer Gegner, plaziert zufällig
    taken = True
    while taken == True:
        a = randint(0,2)
        b = randint(0,2)
        if state[a][b] == 0:
            state[a][b] = 2
            return state

def Game(mode = 0): #Der eigentliche Spielablauf
    state= [[0,0,0], #Das TicTacToe Feld wird als drei Dimensionales Array initialisiert
            [0,0,0],
            [0,0,0]] 
    game = True 
    turn = True
    player = randint(1,2) #beginnender Spieler wird zufällig ausgewürfelt

    while(game == True):
        Draw_Screen(state)
        pl = player
        if pl == 1:
            print('\nTurn of X:')
        else:
            print('\nTurn of O:')
        if player == 1:
            state = player_Move(pl,turn,state)
        elif player == 2 and mode == 0:
            state = mock_AI(state)
        else:
            state = player_Move(pl,turn,state) 
        result = Game_WinCheck(player,state) #wenn noch niemand gewonnen hat wird ein leerer String ausgegeben   
        if result != '': #ist dieser String nicht leer wird nochmal abschließend das Feld aufgezeichnet, gefolgt von "You win" oder "You lose"           
            Draw_Screen(state)
            print('\n'+result)
            game = False
        if player == 1: #Spilerwechsel zwischen den Zügen
            player = 2
        else:
            player = 1 
        turn = True
        print('')

### Anfang #################################################################
while True:
    modd = input('Against COM (default) or another Player? (Enter 2) ')
    if modd == '2':
        Game(2)
    else:
        Game(0)
        
        
