#Tetris in the Console
import time

class Block:
    def __init__(self):
        self.isDropping = True


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
         0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
         1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
         0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

X_DIM = 10
Y_DIM = 22

def draw():
    for y in range(Y_DIM):
        print("|", end='')
        for x in range(X_DIM):
            print(str(getIcon(FIELD[(Y_DIM - 1 - y) * X_DIM + x])),end='')
        print()
    print("|     Welcome to TetrisPY     |")


def getIcon(icon):
    if(icon == 0):
        return '  |'
    elif(icon == 1):
        return ' o|'
    elif(icon == 2):
        return ' x|'
    return ' '

def stopAndWait():
    time.sleep(0.2)

def updateFieldTest():

    for piece in range(X_DIM * Y_DIM):
        if(FIELD[piece] == 1):
            if(piece - X_DIM < 0 or (FIELD[piece - X_DIM] != 0)):
                FIELD[piece] = 2
            else:
                FIELD[piece] = 0
                FIELD[piece - X_DIM] = 3 #auf 3 setzen um updating zu unterbinden

    for piece in range(X_DIM * Y_DIM):
        if(FIELD[piece] == 3):
            FIELD[piece] = 1

    
        

###############################################################################################
while(True):
    draw()
    updateFieldTest()
    stopAndWait()

#Ablaufvorstellung
#blockFaellt() -> drehen, bewegen
#blockLandet() -> checkLines, updateLines, getNewBlock