#字典应用，井字棋盘

theBoard={'top-L':' ','top-M':' ','top-R':' ',
          'mid-L':' ','mid-M':' ','mid-R':' ',
          'low-L':' ','low-M':' ','low-R':' '
         }

# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
#             'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}


def printBoard(board):
    print(board['top-L'] +'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] +'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L'] +'|'+board['low-M']+'|'+board['low-R'])

trun ='X'
for i in range(1,9):
    printBoard(theBoard)
    print('Trun for '+ trun+'.Move on which space?')
    move = input()
    theBoard[move]=trun
    if trun == 'X':
        trun ='O'
    else:
        trun ='X'
printBoard(theBoard)