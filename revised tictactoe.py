import random
print('Welcome to Tictactoe! Have a look at the grid below and enter the coordinates you want to play as and when the prompt comes up')
print('__A1__|__A2__|__A3__')
print('__B1__|__B2__|__B3__')
print('  C1  |  C2  |  C3  ')
grid=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
gridfv=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
lp=[]
lc=[]
e=0
t=0
lt=[1,2]
noto=0
player_name=input('enter your player name: ')
toss=int(input('We shall start with the toss, for calling out heads press 1, for calling out tails press 2: '))
while toss not in lt:
    toss=int(input('enter the right numbers as told to you earlier, if you were not listening, press 1 for heads, press 2 for tails: '))
    noto+=1
    if noto>3:
        print(player_name,', why cant you type the right things?')
        toss=int(input('Last chance,type 1 for heads, 2 for tails, or you will lose the toss anyway: '))
        break
from random import randint
coin=randint(1,2)
if toss==coin:
    print('you have won the toss, you shall make the first move')
    while t==0:
        print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
        print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
        print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
        move=input('Enter the coordinates of your move: ')
        move=move.upper()
        while move.upper() not in grid:
            move=input('Enter the correct coordinates: ')
        move=move.upper()
        lp.append(move)
        gi=grid.index(move)
        grid.remove(move)
        d=gridfv.index(move)
        gridfv.remove(move)
        gridfv.insert(d,' O')
        if 'A1' in lp and 'A2' in lp and 'A3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'B1' in lp and 'B2' in lp and 'B3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lp and 'C2' in lp and 'C3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lp and 'B1' in lp and 'C1' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A2' in lp and 'B2' in lp and 'C2' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A3' in lp and 'B3' in lp and 'C3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lp and 'B2' in lp and 'C3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lp and 'B2' in lp and 'A3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        e+=1
        if e==5:
            print('looks like your enemy is evenly matched with you,',player_name)
            break
        cmove=random.choice(grid)
        print('the computer placed its move on ',cmove)
        lc.append(cmove)
        gi=grid.index(cmove)
        grid.remove(cmove)
        d=gridfv.index(cmove)
        gridfv.remove(cmove)
        gridfv.insert(d,' X')
        if 'A1' in lc and 'A2' in lc and 'A3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'B1' in lc and 'B2' in lc and 'B3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lc and 'C2' in lc and 'C3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lc and 'B1' in lc and 'C1' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A2' in lc and 'B2' in lc and 'C2' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A3' in lc and 'B3' in lc and 'C3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lc and 'B2' in lc and 'C3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lc and 'B2' in lc and 'A3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break



elif toss!=coin:
    print('you have lost the toss, the computer shall make the first move')
    while t==0:
       
        cmove=random.choice(grid)
        print('the computer placed its move on ',cmove)
        lc.append(cmove)
        gi=grid.index(cmove)
        grid.remove(cmove)
        d=gridfv.index(cmove)
        gridfv.remove(cmove)
        gridfv.insert(d,' X')
        print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
        print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
        print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
        if 'A1' in lc and 'A2' in lc and 'A3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'B1' in lc and 'B2' in lc and 'B3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lc and 'C2' in lc and 'C3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lc and 'B1' in lc and 'C1' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A2' in lc and 'B2' in lc and 'C2' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A3' in lc and 'B3' in lc and 'C3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lc and 'B2' in lc and 'C3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lc and 'B2' in lc and 'A3' in lc:
            print('Bad luck ',player_name,' the computer has won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        e+=1
        if e==5:
            print('looks like your enemy is evenly matched with you,',player_name)
            break
        move=input('Enter the coordinates of your move: ')
        move=move.upper()
        while move.upper() not in grid:
            move=input('Enter the correct coordinates: ')
        move=move.upper()
        lp.append(move)
        gi=grid.index(move)
        grid.remove(move)
        d=gridfv.index(move)
        gridfv.remove(move)
        gridfv.insert(d,' O')
        if 'A1' in lp and 'A2' in lp and 'A3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'B1' in lp and 'B2' in lp and 'B3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lp and 'C2' in lp and 'C3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lp and 'B1' in lp and 'C1' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A2' in lp and 'B2' in lp and 'C2' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A3' in lp and 'B3' in lp and 'C3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'A1' in lp and 'B2' in lp and 'C3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
        elif 'C1' in lp and 'B2' in lp and 'A3' in lp:
            print('congratulations! ',player_name,' you have won')
            print('__',gridfv[0],'__|__',gridfv[1],'__|__',gridfv[2],'__')
            print('__',gridfv[3],'__|__',gridfv[4],'__|__',gridfv[5],'__')
            print('  ',gridfv[6],'  |  ',gridfv[7],'  |  ',gridfv[8],'  ')
            t=1
            break
