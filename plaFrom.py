import numpy as np
import threading
from threading import Timer
import time
from tft.tft_api import *
from tft.chess import *
from tft.monster import *

class PlatForm:
    def __init__(self):
        self.arr = [['-' for _ in range(7)] for _ in range(4)]
        self.arr.append(['-' for _ in range(9)])
        self.hasChessLocation = []

    def insertChess(self, row, column, chess):
        self.arr[row][column] = chess
        self.hasChessLocation.append([row, column])
        self.hasChessLocation.sort()

    def chessSwitch(self, row1, column1, row2, column2):
        # if self.arr[row1][column1] != '-' and self.arr[row2][column2] != '-':
        #     self.hasChessLocation.remove([row1, column1])
        self.arr[row1][column1], self.arr[row2][column2] = self.arr[row2][column2], self.arr[row1][column1]
        self.hasChessLocation.append([row2, column2])
        self.hasChessLocation.sort()

    def chessSwitchNoAppend(self, row1, column1, row2, column2):
        self.arr[row1][column1], self.arr[row2][column2] = self.arr[row2][column2], self.arr[row1][column1]

    def printBattleArr(self):
        start = time.time()
        while True:
            if time.time() - start > 5:
                break
            for i in range(4):
                for j in range(7):
                    if self.arr[i][j] != '-':
                        print(bcolors.OK + '{:4}'.format(self.arr[i][j].getName()), end=' ' + bcolors.RESET)
                    else:
                        print('{:4}'.format(self.arr[i][j]), end=' ')
                print()
            print(bcolors.FAIL + "-" * 40 + bcolors.RESET)
            clearConsole()

    
    def printPrepareArr(self):
        i = 4
        for j in range(9):
            if self.arr[i][j] != '-':
                print(bcolors.OK + '{:3}'.format(self.arr[i][j].getName()), end=' ' + bcolors.RESET)
            else:
                print(bcolors.WARNING + '{:3}'.format(self.arr[i][j]), end=' ' + bcolors.RESET)
    
    def move(self):
        for i in range(len(self.hasChessLocation)):
            t = threading.Thread(target = self.moveThread, args = (self.hasChessLocation[i],))
            t.start()
    
    def moveThread(self, loc):
        row = loc[0]
        column = loc[1]
        while row > 0:
            time.sleep(self.arr[row][column].MS)
            self.chessSwitchNoAppend(row, column, row-1, column)
            row -= 1

def battle(p1, p2):
    for i in range(len(p2.hasChessLocation)):
        for j in range(len(p1.hasChessLocation)):
            t = threading.Thread(target=battleThread, args=(p1, j, p2, i))


def battleThread(p1, j, p2, i):
    row1 = p1.hasChessLocation[j][0]
    column1 = p1.hasChessLocation[j][1]
    row2 = p2.hasChessLocation[i][0]
    column2 = p2.hasChessLocation[i][1]
    p1.arr[row1][column1].AT = p2.arr[row2][column2]

# def reverseArr(arr):
#     arr = arr[::-1]
#     arr = arr[1:]
#     for i in range(4):
#         arr[i].reverse()

#     return arr

# def reverseHasChessLocation(hasChessLocation):
#     for i in range(len(hasChessLocation)):
#         hasChessLocation[i][0] = abs(hasChessLocation[i][0] - 3)
#         hasChessLocation[i][1] = abs(hasChessLocation[i][1] - 6)
#         print(hasChessLocation[i])
#     return hasChessLocation

platForm1 = PlatForm()
platForm2 = PlatForm()

# printT = threading.Thread(target = platForm1.printBattleArr)
# printT.start()

poppy_1 = Poppy()
poppy_2 = Poppy()
poppy_3 = Poppy()
dragon = Dragon()

platForm2.insertChess(0, 3, dragon)
platForm2.insertChess(3, 1, poppy_1)
# ziggs_1 = Ziggs()
# ziggs_2 = Ziggs()
# ziggs_3 = Ziggs()

platForm1.insertChess(3, 4, poppy_1)
platForm1.insertChess(3, 2, poppy_2)
platForm1.insertChess(2, 6, poppy_3)

# platForm2.insertChess(1, 5, poppy_3)
# platForm2.insertChess(3, 6, ziggs_2)
# platForm2.insertChess(3, 1, ziggs_3)

# platForm1.chessSwitch(0, 0, 3, 4)
# platForm1.chessSwitch(3, 2, 3, 2)
# platForm1.chessSwitch(2, 6, 2, 6)


# platForm1.move()

battle(platForm1, platForm2)