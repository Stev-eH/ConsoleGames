#Tetris in the Console
import time
import os
from enum import IntEnum

####### EDITABLE OPTIONS #################################

DEBUG_FUNC = 1 #Enables Debug Functionality if set to 1
TIMER_DELAY = 0.2 #Sets the update freuquency

##########################################################

class Block:
    def __init__(self):
        self.isDropping = True

class State(IntEnum):
    EMPTY = 0
    FALLING = 1
    SET = 2
    FULLLINE = 3
    CLEAR_BLINK_ON = 4
    CLEAR_BLINK_OFF = 5
    UPDATE_LOCK = 6


FIELD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
         0, 0, 0, 0, 0, 0, 1, 1, 0, 0]

X_DIM = 10
Y_DIM = 22


def draw():

    clear()

    #Empty line for better readability
    print()

    for y in range(Y_DIM):
        print("|", end='')
        for x in range(X_DIM):
            print(str(getIcon(FIELD[FieldFormula(x,y)])),end='')
            # FieldFormula = ((Y_DIM - 1 - y) * X_DIM + x)
        print(y if DEBUG_FUNC == 1 else '')

    print("|     Welcome to TetrisPY     |")


def getIcon(icon):

    if(icon == State.EMPTY):
        return '  |'
    
    elif(icon == State.FALLING):
        return ' o|'
    
    elif(icon == State.SET):
        return ' x|'
    
    elif(icon == State.FULLLINE):
        return ' ~|'
    
    return ' '


def stopAndWait():
    time.sleep(TIMER_DELAY)


def updateFieldTest():

    pieceSet = False

    for piece in range(X_DIM * Y_DIM):
        if(FIELD[piece] == State.FALLING and pieceSet == False):
            if(piece - X_DIM < 0 or (FIELD[piece - X_DIM] != State.EMPTY)):
                pieceSet = True
            else:
                FIELD[piece] = State.EMPTY
                FIELD[piece - X_DIM] = State.UPDATE_LOCK #auf UPDATE_LOCK setzen um updating zu unterbinden

    for piece in range(X_DIM * Y_DIM):
        if(FIELD[piece] == State.UPDATE_LOCK):
            FIELD[piece] = State.FALLING

    if(pieceSet):
        for piece in range(X_DIM * Y_DIM):
            if(FIELD[piece] == State.FALLING):
                FIELD[piece] = State.SET


def updateFieldAfterLineClear(yCleared):

    for y in range(yCleared + 1, 0, -1):
        for x in range(X_DIM):
            if(y == yCleared):
                FIELD[FieldFormula(x,y)] = 0
        for x in range(X_DIM):
            # FieldFormula = ((Y_DIM - 1 - y) * X_DIM + x)
            FIELD[FieldFormula(x,y + 1)] = FIELD[FieldFormula(x,y)]


def clear(): #clear() leert die Konsolenansicht

    command = ''
    if os.name == 'nt':
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)


def checkFullLine():

    for y in range(Y_DIM):
        full = True
        for x in range(X_DIM):
            if(FIELD[FieldFormula(x,y)] == 0):
                full = False

        if(full):
            for x in range(X_DIM):
                FIELD[FieldFormula(x,y)] = 5
            return y
        
    return -1


def FieldFormula(x, y):
    return ((Y_DIM - 1 - y) * X_DIM + x)

    
        

###############################################################################################
while(True):
    draw()
    updateFieldTest()
    yCleared = checkFullLine()
    print(yCleared) if DEBUG_FUNC == 1 else ''
    if(yCleared >= 0):
        print("Called" if DEBUG_FUNC == 1 else '')
        updateFieldAfterLineClear(yCleared)
    stopAndWait()

#Ablaufvorstellung
#blockFaellt() -> drehen, bewegen
#blockLandet() -> checkLines, updateLines, getNewBlock