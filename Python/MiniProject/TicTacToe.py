import os
upperr = '*'*17
lower = '*'*17
gutter = '*  ---|---|---  *'
pawn_line = '*   {} | {} | {}   *'

# print(pawn_line.format(xo[0,0],xo[0,1],xo[0,2]))



xo = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']
]
# x1o = [
#     [' ',' ',' '],
#     [' ',' ',' '],
#     [' ',' ',' ']
# ] 




def printBoard(xo):
    
    print(upperr)
    print(pawn_line.format(xo[0][0],xo[0][1],xo[0][2]))
    print(gutter)
    print(pawn_line.format(xo[1][0],xo[1][1],xo[1][2]))
    print(gutter)
    print(pawn_line.format(xo[2][0],xo[2][1],xo[2][2]))
    print(gutter)
    print(lower)

# print(printBoard(xo))

def checkWinEnd(xo,pawn):
    xot=list(zip(*xo))
    for i in (0,1,2):
        if ''.join(xo[i]) == pawn*3: return True
        if ''.join(xot[i]) == pawn*3: return True
    if (xo[0][0],xo[1][1],xo[2][2]) == (pawn,pawn,pawn): return True
    if (xo[0][2],xo[1][1],xo[2][0]) == (pawn,pawn,pawn): return True
    return False

def updateBoard(xo,names_dict,player_name):
    coor = str(input('it is {}\'s turn. select x location (format:xy 0-2): '.format(player_name)))

    while not((coor in ['00','01','02','10','11','12','20','21','22']) and (isCoorVacant(xo,*coor))):
        print('corr not in corret ')
        coor = str(input('it is {}\'s turn. select x location (format:xy 0-2): '.format(player_name)))
        
    x=int(coor[0])
    y=int(coor[1])

    xo[x][y] = names_dict[player_name]
    
    return True

def isCoorVacant(xo,x,y):
    x=int(x)
    y=int(y)
    vacant = xo[x][y] == ' '
    if vacant: return True
    print('location is oocupied')
    return False


players=['','']
players[0] = str(input('X player name: '))
players[1] = str(input('O player name: '))

names_dict=dict()
names_dict[players[0]]='X'
names_dict[players[1]]='O'
i=1

while not checkWinEnd(xo,names_dict[players[i]]):
    i = (i+1) % 2
    
    player_name = players[i]
    pawn = names_dict[players[i]]
    # print('i is {} player{} {}'.format(i,player_name,pawn))
    os.system('cls')
    printBoard(xo)

    updateBoard(xo,names_dict,player_name)
    
    
printBoard(xo)
print('{} has won'.format(names_dict[players[i]]))
    



# make 02 or 11 to 0,2 1,1 withouy asking x and y
# handle end game

# *****************
# *     |   |     *
# *  ---|---|---  *
# *    |  |    *
# *  ---|---|---  *
# *    |  |    *
# *  ---|---|---  *
# *****************


