import os

#printBoard will print the current status of the board nicely with decoration
def printBoard():
    
    print(upperr)
    print(pawn_line.format(xo[0][0],xo[0][1],xo[0][2]))
    print(gutter)
    print(pawn_line.format(xo[1][0],xo[1][1],xo[1][2]))
    print(gutter)
    print(pawn_line.format(xo[2][0],xo[2][1],xo[2][2]))
    print(lower)


# checkWinEnd checks if the game has ended by a win
# True if there a win 
#False if there is no win
def Win(xo,player_pawn):
    xot = list(zip(*xo))
    for i in [0,1,2]:
        if ''.join(xo[i]) == player_pawn*3: return True #winning row
        if ''.join(xot[i]) == player_pawn*3: return True #winnig column
    if (xo[0][0],xo[1][1],xo[2][2]) == (player_pawn,player_pawn,player_pawn): return True #wining diagonal
    if (xo[0][2],xo[1][1],xo[2][0]) == (player_pawn,player_pawn,player_pawn): return True #wining secongdiagonal
    return False #none

    
# updateBoard is asking thae user for input and vaidate
# once validate it will update the obrad accordingly

def updateBoard(xo,player_pawn,player_name):
    coor = str(input('it is {}\'s turn. select x location (format:xy 0-2): '.format(player_name)))
  
    while isWrongFormat(coor):
        coor = str(input('it is {}\'s turn. select x location (format:xy 0-2): '.format(player_name)))
        
    x=int(coor[0])
    y=int(coor[1])
    xo[x][y] = player_pawn
    
    return True

# checking if input is in wrong format
# if format is correct and if location seleted is vacant
def isWrongFormat(coor):
    if coorCorrectFormat(coor):
        if isCoorVacant(xo,*coor):
            return False #coor not wrong format and not vacant
        return True #coor is not good - not vacant
    return True #coor  not good - not good format

#check if input in correct format of either '00','01','02','10','11','12','20','21','22'
def coorCorrectFormat(coor):
    if coor in ['00','01','02','10','11','12','20','21','22']:
        return True #corr is in correct format
    print('corr not in corret format') # message to user why input no good
    return False #coor is in wrong format


# check i location is vacant
# this method will only be called if coorCorrectFormat has determined the format is correct.
def isCoorVacant(xo,x,y):
    x=int(x)
    y=int(y)
    vacant = xo[x][y] == ' '
    if vacant: return True #in cease location is vacant
    print('location is oocupied')# message to user why input no good
    return False #location is not vacant



# visual display of board will 

upperr = '*'*17
lower = '*'*17
gutter = '*  ---|---|---  *'
pawn_line = '*   {} | {} | {}   *'

# xo is the pawn location manager. 
# xo is reset to have all vacant
xo = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


# clean board
os.system('cls')
printBoard()

# setting player-pawn dictionary
#the list contain each player dictionari
player_names=[dict(),dict()]
player_names[0] = {str(input('X player name: ')) : 'X'} # prompting user for X' name
player_names[1] = {str(input('O player name: ')) : 'O'} # prompting user for 0' name


current_player_index=1 #initializing the player to the second. current_player_index will be 0 or 1
turns_count = 9 # in case of tie need to end game after 9 turns

#intializing values for first while condition
player_name = list(player_names[current_player_index].keys())[0]
player_pawn = list(player_names[current_player_index].values())[0]

while (not Win(xo,player_pawn)) and 0 < turns_count:            # previous user did not win and there are turns left
    current_player_index = (current_player_index+1) % 2         # switch user
    player_name = list(player_names[current_player_index].keys())[0]    
    player_pawn = list(player_names[current_player_index].values())[0]
    os.system('cls')
    printBoard()
    updateBoard(xo,player_pawn,player_name)                     # update the board by asking input, validating, and updating the board(xo)
    turns_count -= 1

#game has a winner or no turns left. lets check:
if Win(xo,player_pawn):                                         #if we are kicked of while loop because there a winner it can only be current_player_index
    os.system('cls')
    printBoard()
    print('{} has won'.format(player_name))
else:                                                           #if kicked not because winnr then tie
    os.system('cls')
    printBoard()
    print(' game has ended with a tie')
    