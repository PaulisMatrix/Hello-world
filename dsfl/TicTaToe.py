import sys

theBoard={'top-L':' ','top-M':' ','top-R':' ',
          'mid-L':' ','mid-M':' ','mid-R':' ',
          'low-L':' ','low-M':' ','low-R':' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] )
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] )
printBoard(theBoard)  #prints the board format


#function to quit the game
def end(move):
    if move=='quit':
        sys.exit()

#function to check if any player has won
def check_board(board,turn):
    win_conditions=[
        ['top-L','top-M','top-R'],
        ['mid-L','mid-M','mid-R'],
        ['low-L','low-M','mid-R'],
        ['top-L','mid-L','low-L'],
        ['top-M','mid-M','low-M'],
        ['top-R','mid-R','low-R'],
        ['top-L','mid-M','low-R'],
        ['low-L','mid-M','top-R'],
        ]
    for conditions in win_conditions:
        if (board[conditions[0]] != ' ' and board[conditions[0]] == board[conditions[1]] == board[conditions[2]]):
         #if  (board[conditions[0]  !=' '  and board[conditions[0]] == board[conditions[1]] == board[conditions[2]]):
           printBoard(board)
           print( turn + ' wins\n')
           print("Would you like to play agains ( type yes to continue) ? ")
           answer=input()
           if (answer=='yes'):
               return answer
           else:
               sys.exit()
           
turn='X'
move=' '
print('\nTo choose a position, type in which row(top, mid, low) followed by which column(-R, -M, -L')
print('To move to the top left corner, you would type "top-L", bottom mid would be "low-M", without the quotes.')
while move!='quit':
    printBoard(theBoard)
    print('Turn for the ' + turn + ' move in which space? ')
    move=input()
    end(move)
    if (move not in theBoard):
           print("Try again!")
           continue
    elif ( theBoard[move]==' '):
           theBoard[move]=turn
    else:
           print("Try again!")
           continue
    #check_board(theBoard,turn)
    if( check_board(theBoard,turn) == 'yes'):
        for i in theBoard:
            theBoard[i]=' '  
    if turn=='X':
        turn='O'
    else:
        turn='X'
           
printBoard(theBoard)
