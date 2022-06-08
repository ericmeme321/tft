import numpy as np
import pandas as pd

levelRatio = {'1': [1,0,0,0,0],
            '2': [1,0,0,0,0],
            '3': [0.75,0.25,0,0,0],
            '4': [0.55,0.3,0.15,0,0],
            '5': [0.45,0.33,0.2,0.2,0],
            '6': [0.25,0.4,0.3,0.05,0],
            '7': [0.19,0.3,0.35,0.15,0.01],
            '8': [0.16,0.2,0.35,0.25,0.04],
            '9': [0.09,0.15,0.3,0.3,0.16],
            '10': [0.05,0.1,0.2,0.4,0.2],
            '11': [0.01,0.02,0.12,0.5,0.35]}

oneStarChessData = {
    "name": ["Ziggs", "Brand", "Caitlyn", "Camille", "Darius", "Ezreal", "Illaoi", "Jarvan IV", "Kassadin", "Nocturne", "Poppy", "Singed", "Twitch"],
    "numbers": [39] * 13,
    "ratio": [0] * 13
}

twoStarChessData = {
    "name": ["Ashe", "Blitzcrank", "Corki", "Lulu", "Quinn", "RekSai", "Sejuani", "Swain", "Syndra", "Talon", "Warwick", "Zilean", "Zyra"],
    "numbers": [26] * 13,
    "ratio": [0] * 13
}

threeStarChessData = {
    "name": ["Chogath", "Ekko", "Gangplank", "Gnar", "Leona", "Lucian", "Malzahar", "Miss Fortune", "Morgana", "Senna", "Tryndamere", "Vex", "Zac",],
    "numbers": [21] * 13,
    "ratio": [0] * 13
}

fourStarChessData = {
    "name": ["Ahri", "Alistar", "Braun", "Draven", "Irelia", "Jhin", "Khazix", "Orianna", "Renata Glasc", "Seraphine", "Sivir", "Vi",],
    "numbers": [13] * 12,
    "ratio": [0] * 12
}

fiveStarChessData = {
    "name": ["Galio", "Jayce", "Jinx", "Kaisa", "Silco", "Tahm Kench", "Viktor", "Zeri",],
    "numbers": [10] * 8,
    "ratio": [0] * 8
}

oneStarDf = pd.DataFrame(oneStarChessData)
twoStarDf = pd.DataFrame(twoStarChessData)
threeStarDf = pd.DataFrame(threeStarChessData)
fourStarDf = pd.DataFrame(fourStarChessData)
fiveStarDf = pd.DataFrame(fiveStarChessData)

starNumbers = [13, 13, 13, 12, 8]
level = "1"
# starNumbers = 100 / np.array(starNumbers)


def toAddnumber(number, df):
    print(df)
    chessOption = input("加哪個棋子:")
    addNumber = input("加多少:")
    chessOption = int(chessOption)
    addNumber = int(addNumber)

    if chessOption < starNumbers[number-1] and chessOption >= 0:
        temp = df.loc[chessOption,'numbers'] + addNumber
        df.loc[chessOption,'numbers'] = temp
    
    print()

    return df

def toSubnumber(number, df):
    print(df)
    chessOption = input("減哪個棋子:")
    addNumber = input("減多少:")
    chessOption = int(chessOption)
    addNumber = int(addNumber)

    if chessOption < starNumbers[number-1] and chessOption >= 0:
        temp = df.loc[chessOption,'numbers'] - addNumber
        df.loc[chessOption,'numbers'] = temp      
    print()

    return df

def toFindnumber(number, df, level):
    for i in range(0,starNumbers[number-1]):
        tempRatio = levelRatio[level][number-1] * df.loc[i, 'numbers'] / df['numbers'].sum()
        df.loc[i, 'ratio'] = str(np.round(tempRatio * 100, decimals=3)) + ' %'
    print(df)
    print()

    return

if __name__ == '__main__':
    while True:
        curLevel = input("指令: ")
        if curLevel.isdigit():
            if int(curLevel) > 0 and int(curLevel) < 12:
                print(levelRatio[curLevel])
                level = curLevel
                print("等級已更改")
                print()
        # elif curLevel == '*':
        #     print(oneStarDf)
        #     print(twoStarDf)
        #     print(threeStarDf)
        #     print(fourStarDf)
        #     print(fiveStarDf)
        elif len(curLevel) == 2 and curLevel[1].isdigit():
            number = int(curLevel[1])
            if curLevel[0] == '+':
                if number == 1:
                    oneStarDf = toAddnumber(number, oneStarDf)
                    toFindnumber(number, oneStarDf, level)
                elif number == 2:
                    twoStarDf = toAddnumber(number, twoStarDf)
                    toFindnumber(number, twoStarDf, level)
                elif number == 3:
                    threeStarDf = toAddnumber(number, threeStarDf)
                    toFindnumber(number, threeStarDf, level)
                elif number == 4:
                    fourStarDf = toAddnumber(number, fourStarDf)
                    toFindnumber(number, fourStarDf, level)
                elif number == 5:
                    fiveStarDf = toAddnumber(number, fiveStarDf)
                    toFindnumber(number, fiveStarDf, level)
            elif curLevel[0] == '-':
                if number == 1:
                    oneStarDf = toSubnumber(number, oneStarDf)
                    toFindnumber(number, oneStarDf, level)
                elif number == 2:
                    twoStarDf = toSubnumber(number, twoStarDf)
                    toFindnumber(number, twoStarDf, level)
                elif number == 3:
                    threeStarDf = toSubnumber(number, threeStarDf)
                    toFindnumber(number, threeStarDf, level)
                elif number == 4:
                    fourStarDf = toSubnumber(number, fourStarDf)
                    toFindnumber(number, fourStarDf, level)
                elif number == 5:
                    fiveStarDf = toSubnumber(number, fiveStarDf)
                    toFindnumber(number, fiveStarDf, level)
            elif curLevel[0] == '.':
                if number == 1:
                    toFindnumber(number, oneStarDf, level)
                elif number == 2:
                    toFindnumber(number, twoStarDf, level)
                elif number == 3:
                    toFindnumber(number, threeStarDf, level)
                elif number == 4:
                    toFindnumber(number, fourStarDf, level)
                elif number == 5:
                    toFindnumber(number, fiveStarDf, level)

