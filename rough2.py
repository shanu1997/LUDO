from colorama import Fore
import random
import os
r1=None;r2=None;r3=None;r4=None
g1=None;g2=None;g3=None;g4=None
y1=None;y2=None;y3=None;y4=None
b1=None;b2=None;b3=None;b4=None
dice=None;turn_clr=None
peice_select=None;user_input=None
red=[r1,r2,r3,r4]
green=[g1,g2,g3,g4]
yellow=[y1,y2,y3,y4]
blue=[b1,b2,b3,b4]
main=[red,green,yellow,blue,turn_clr,dice,user_input]
c=['red','green','yellow','blue']
def dice():
    interface()
    global main
    enter=input("PRESS ENTER TO ROLL DICE")
    main[5]=random.randint(1,6)
    peice_process()
def turn():
    interface()
    global main
    if main[4]==None:
        main[4]=c[0]
    else:
        if main[4]==c[len(c)-1]:
            main[4]=c[0]
        else:
            main[4]=c[c.index(main[4])+1]
    dice()
def peice_process():
    interface()
    global main
    if main[5]==6:
        try:
            main[6]=int(input("SELECT INTEGER FROM 1 TO 4\n"))
        except:
            main[6]=random.randint(1,4)
        if main[c.index(main[4])][main[6]-1]==None:
            main[c.index(main[4])][main[6]-1]=0
            turn()
        elif main[c.index(main[4])][main[6]-1]+main[5]>56:
            print("SELECT ANOTHER 1")
            peice_process()
        else:
            main[c.index(main[4])][main[6]-1]+= main[5]
            peice_ruleout()
    else:
        if main[c.index(main[4])][0]==main[c.index(main[4])][1]==main[c.index(main[4])][2]==main[c.index(main[4])][3]==None:
            print("OOPS!")
            turn()
        else:
            try:
                main[6]=int(input("SELECT INTEGER FROM 1 TO 4\n"))
            except:
                main[6]=random.randint(1,4)
            if main[c.index(main[4])][main[6]-1]!= None and main[c.index(main[4])][main[6]-1]+main[5]<= 56:
                main[c.index(main[4])][main[6]-1]+= main[5]
                peice_ruleout()
            else:
                print("SELECT ANOTHER 1")
                peice_process()

def peice_ruleout():
    interface()
    global main
    if main[4]=='red':
            if main[0][main[6]-1]== 0 or main[0][main[6]-1]== 8 or main[0][main[6]-1]== 13 or main[0][main[6]-1]== 21 or main[0][main[6]-1]== 26 or main[0][main[6]-1]== 34 or main[0][main[6]-1]== 39 or main[0][main[6]-1]== 47 or main[0][main[6]-1]> 50:
                print("YOU'RE ON STAR")
                turn()
            if main[0][main[6]-1]- 13==main[1][0]:
                main[1][main[6]-1]= None
                dice()
            if main[0][main[6]-1]- 13==main[1][1]:
                main[1][1]=None
                dice()
            if main[0][main[6]-1]- 13==main[1][2]:
                main[1][2]=None
                dice()
            if main[0][main[6]-1]- 13==main[1][3]:
                main[1][3]=None
                dice()
            if main[0][main[6]-1]- 26==main[2][0]:
                main[2][main[6]-1]= None
                dice()
            if main[0][main[6]-1]- 26==main[2][1]:
                main[2][1]=None
                dice()
            if main[0][main[6]-1]- 26==main[2][2]:
                main[2][2]=None
                dice()
            if main[0][main[6]-1]- 26==main[2][3]:
                main[2][3]=None
                dice()
            if main[0][main[6]-1]- 39==main[3][0]:
                main[3][main[6]-1]= None
                dice()
            if main[0][main[6]-1]- 39==main[3][1]:
                main[3][1]=None
                dice()
            if main[0][main[6]-1]- 39==main[3][2]:
                main[3][2]=None
                dice()
            if main[0][main[6]-1]- 39==main[3][3]:
                main[3][3]=None
                dice()
            else:
                if main[5]==6:
                    dice()
                else:
                    turn()
    if main[4]=='green':
            if main[1][main[6]-1]== 0 or main[1][main[6]-1]== 8 or main[1][main[6]-1]== 13 or main[1][main[6]-1]== 21 or main[1][main[6]-1]== 26 or main[1][main[6]-1]== 34 or main[1][main[6]-1]== 39 or main[1][main[6]-1]== 47 or main[1][main[6]-1]> 50:
                print("YOU'RE ON STAR")
                turn()
            if main[1][main[6]-1]-39==main[0][0]:
                main[0][main[6]-1]=None
                dice()
            if main[1][main[6]-1]-39==main[0][1]:
                main[0][1]=None
                dice()
            if main[1][main[6]-1]-39==main[0][2]:
                main[0][2]=None
                dice()
            if main[1][main[6]-1]-39==main[0][3]:
                main[0][3]=None
                dice()
            if main[1][main[6]-1]- 13==main[2][0]:
                main[2][main[6]-1]= None
                dice()
            if main[1][main[6]-1]- 13==main[2][1]:
                main[2][1]=None
                dice()
            if main[1][main[6]-1]- 13==main[2][2]:
                main[2][2]=None
                dice()
            if main[1][main[6]-1]- 13==main[2][3]:
                main[2][3]=None
                dice()
            if main[1][main[6]-1]- 26==main[3][0]:
                main[3][main[6]-1]= None
                dice()
            if main[1][main[6]-1]- 26==main[3][1]:
                main[3][1]=None
                dice()
            if main[1][main[6]-1]- 26==main[3][2]:
                main[3][2]=None
                dice()
            if main[1][main[6]-1]- 26==main[3][3]:
                main[3][3]=None
                dice()
            else:
                if main[5]==6:
                    dice()
                else:
                    turn()

    if main[4]=='yellow' :
            if main[2][main[6]-1]== 0 or main[2][main[6]-1]== 8 or main[2][main[6]-1]== 13 or main[2][main[6]-1]== 21 or main[2][main[6]-1]== 26 or main[2][main[6]-1]== 34 or main[2][main[6]-1]== 39 or main[2][main[6]-1]== 47 or main[2][main[6]-1]> 50:
                print("YOU'RE ON STAR")
                turn()
            if main[2][main[6]-1]- 26==main[0][0]:
                main[0][main[6]-1]= None
                dice()
            if main[2][main[6]-1]- 26==main[0][1]:
                main[0][1]=None
                dice()
            if main[2][main[6]-1]- 26==main[0][2]:
                main[0][2]=None
                dice()
            if main[2][main[6]-1]- 26==main[0][3]:
                main[0][3]=None
                dice()
            if main[2][main[6]-1]- 39==main[1][0]:
                main[1][main[6]-1]= None
                dice()
            if main[2][main[6]-1]- 39==main[1][1]:
                main[1][1]=None
                dice()
            if main[2][main[6]-1]- 39==main[1][2]:
                main[1][2]=None
                dice()
            if main[2][main[6]-1]- 39==main[1][3]:
                main[1][3]=None
                dice()
            if main[2][main[6]-1]- 13==main[3][0]:
                main[3][main[6]-1]= None
                dice()
            if main[2][main[6]-1]- 13==main[3][1]:
                main[3][1]=None
                dice()
            if main[2][main[6]-1]- 13==main[3][2]:
                main[3][2]=None
                dice()
            if main[2][main[6]-1]- 13==main[3][3]:
                main[3][3]=None
                dice()
            else:
                if main[5]==6:
                    dice()
                else:
                    turn()

    if main[4]=='blue':
            if main[3][main[6]-1]== 0 or main[3][main[6]-1]== 8 or main[3][main[6]-1]== 13 or main[3][main[6]-1]== 21 or main[3][main[6]-1]== 26 or main[3][main[6]-1]== 34 or main[3][main[6]-1]== 39 or main[3][main[6]-1]== 47 or main[3][main[6]-1]> 50:
                print("YOU'RE ON STAR")
                turn()
            if main[3][main[6]-1]- 13==main[0][0]:
                main[0][main[6]-1]= None
                dice()
            if main[3][main[6]-1]- 13==main[0][1]:
                main[0][1]=None
                dice()
            if main[3][main[6]-1]- 13==main[0][2]:
                main[0][2]=None
                dice()
            if main[3][main[6]-1]- 13==main[0][3]:
                main[0][3]=None
                dice()
            if main[3][main[6]-1]- 26==main[1][0]:
                main[1][main[6]-1]= None
                dice()
            if main[3][main[6]-1]- 26==main[1][1]:
                main[1][1]=None
                dice()
            if main[3][main[6]-1]- 26==main[1][2]:
                main[1][2]=None
                dice()
            if main[3][main[6]-1]- 26==main[1][3]:
                main[1][3]=None
                dice()
            if main[3][main[6]-1]- 39==main[2][0]:
                main[2][main[6]-1]= None
                dice()
            if main[3][main[6]-1]- 39==main[2][1]:
                main[2][1]=None
                dice()
            if main[3][main[6]-1]- 39==main[2][2]:
                main[2][2]=None
                dice()
            if main[3][main[6]-1]- 39==main[2][3]:
                main[2][3]=None
                dice()
            else:
                if main[5]==6:
                    dice()
                else:
                    turn()
def interface():
    global main
 # interface colours .......................................................................................................................................................................................
    dp=Fore.WHITE+':'
    d=[[dp for x in range(15)]for x in range(15)]
    common_path=[dp for x in range(53)]
    red_path=[[dp,dp,dp,dp],dp,dp,dp,dp,dp,dp]
    green_path=[[dp,dp,dp,dp],dp,dp,dp,dp,dp,dp]
    yellow_path=[[dp,dp,dp,dp],dp,dp,dp,dp,dp,dp]
    blue_path=[[dp,dp,dp,dp],dp,dp,dp,dp,dp,dp]
    for i in range(6):
        common_path[1]=d[0][i]=d[i][0]=d[5][i]=d[i][5]=red_path[i+1]=Fore.RED+':'
        common_path[14]=d[i+9][0]=d[9][i]=d[i+9][5]=d[14][i]=green_path[i+1]=Fore.GREEN+':'
        common_path[27]=d[14][i+9]=d[i+9][14]=d[9][i+9]=d[i+9][9]=yellow_path[
            i+1]=Fore.YELLOW+':'
        common_path[40]=d[i][14]=d[0][i+9]=d[5][i+9]=d[i][9]=blue_path[i+1]=Fore.BLUE+':'
    for i in range(6,9):
        d[i][i]=Fore.MAGENTA+'X'
    d[6][8]=d[8][6]=Fore.MAGENTA+'X'
    for i in range(9,49,13):
        common_path[i]=Fore.WHITE+"*"
    # interface function.......................................................................................................................................................................................
    for x in range(4):
        for y in range(4):
            if main[x][y]==None:
                if x==0:
                    red_path[0][y]=Fore.RED+str(y+1)
                elif x==1:
                    green_path[0][y]=Fore.GREEN+str(y+1)
                elif x==2:
                    yellow_path[0][y]=Fore.YELLOW+str(y+1)
                elif x==3:
                    blue_path[0][y]=Fore.BLUE+str(y+1)
            elif main[x][y]>51:
                if x==0:
                    red_path[main[x][y]-51]=Fore.RED+str(y+1)
                elif x==1:
                    green_path[main[x][y]-51]=Fore.GREEN+str(y+1)
                elif x==2:
                    Yellow_path[main[x][y]-51]=Fore.YELLOW+str(y+1)
                elif x==3:
                    blue_path[main[x][y]-51]=Fore.BLUE+str(y+1)
            else:
                if x==0:
                    common_path[main[x][y]+1]=Fore.RED+str(y+1)
                elif x==1:
                    if main[x][y]<39:
                        common_path[main[x][y]+14]=Fore.GREEN+str(y+1)
                    elif main[x][y]>26:
                        common_path[main[x][y]-38]=Fore.GREEN+str(y+1)
                    else:
                        common_path[0]=Fore.GREEN+str(y+1)
                elif x==2:
                    if main[x][y]<26:
                        common_path[main[x][y]+27]=Fore.YELLOW+str(y+1)
                    elif main[x][y]>26:
                        common_path[main[x][y]-25]=Fore.YELLOW+str(y+1)
                    else:
                        common_path[0]=Fore.YELLOW+str(y+1)
                elif x==3:
                    if main[x][y]<13:
                        common_path[main[x][y]+40]=Fore.BLUE+str(y+1)
                    elif main[x][y]>13:
                        common_path[main[x][y]+12]=Fore.BLUE+str(y+1)
                    else:
                        common_path[0]=Fore.BLUE+str(y+1)
    # dice logo................................................................................................................................................................................................
    if main[5]==1:
        d1=d2=d3=d5=d6=d7=' '
        d4='1'
    elif main[5]==2:
        d2=d3=d5=d6=d4=' '
        d1=d7='2'
    elif main[5]==3:
        d2=d3=d5=d6=' '
        d1=d7=d4='3'
    elif main[5]==4:
        d3=d4=d5=' '
        d1=d2=d6=d7='4'
    elif main[5]==5:
        d3=d5=d4=' '
        d1=d2=d6=d7=d4='5'
    elif main[5]==6:
        d4=' '
        d1=d2=d3=d6=d5=d7='6'
    else:
        d1=d2=d3=d4=d5=d6=d7=' '
    #turn colour indicator...................................................................................................................................................................................
    if main[4]=='red':
        s=Fore.RED+"0"
    elif main[4]=='green':
        s=Fore.GREEN+"0"
    elif main[4]=='yellow':
        s=Fore.YELLOW+"0"
    elif main[4]=='blue':
        s=Fore.BLUE+"0"
    else:
        s="0"
    # print function for whole window..........................................................................................................................................................................
    vb=Fore.WHITE+'|';
    hb=Fore.WHITE+'-'
    os.system('cls')
    print(hb*188)
    print(vb," "*50,vb,d[0][0]*3,' ',d[1][0]*3,' ',d[2][0]*3,' ',d[3][0]*3,' ',d[4][0]*3,' ',d[5][0]*3,' ',common_path[11]*3,' ',common_path[12]*3,' ',common_path[13]*3,' ',d[9][0]*3,' ',d[10][0]*3,' ',d[11][0]*3,' ',d[12][0]*3,' ',d[13][0]*3,' ',d[14][0]*3,' ',vb,s*14,":",d1,' ',d2,":",s*14,vb)
    print(vb," "*50,vb,d[0][0]*3,' ',d[1][0]*3,' ',d[2][0]*3,' ',d[3][0]*3,' ',d[4][0]*3,' ',d[5][0]*3,' ',common_path[11]*3,' ',common_path[12]*3,' ',common_path[13]*3,' ',d[9][0]*3,' ',d[10][0]*3,' ',d[11][0]*3,' ',d[12][0]*3,' ',d[13][0]*3,' ',d[14][0]*3,' ',vb,s*14,":",d3,d4,d5,":",s*14,vb)
    print(vb,Fore.GREEN+"GREEN STAR",hb*39,vb,d[0][1]*3,' ',d[1][1]*3,' ',d[2][1]*3,' ',d[3][1]*3,' ',d[4][1]*3,' ',d[5][1]*3,' ',common_path[10]*3,' ',green_path[1]*3,' ',common_path[14]*3,' ',d[9][1]*3,' ',d[10][1]*3,' ',d[11][1]*3,' ',d[12][1]*3,' ',d[13][1]*3,' ',d[14][1]*3,' ',vb,s*14,":",d6,' ',d7,":",s*14,vb)
    print(vb,"0 "*16," "*17,vb,d[0][1]*3,' ',d[1][1]*3,' ',d[2][1]*3,' ',d[3][1]*3,' ',d[4][1]*3,' ',d[5][1]*3,' ',common_path[10]*3,' ',green_path[1]*3,' ',common_path[14]*3,' ',d[9][1]*3,' ',d[10][1]*3,' ',d[11][1]*3,' ',d[12][1]*3,' ',d[13][1]*3,' ',d[14][1]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][2]*3,' ',d[1][2]*3,' ',red_path[0][0]*3,' ',red_path[0][1]*3,' ',d[4][2]*3,' ',d[5][2]*3,' ',common_path[9]*3,' ',green_path[2]*3,' ',common_path[15]*3,' ',d[9][2]*3,' ',d[10][2]*3,' ',green_path[0][0]*3,' ',green_path[0][1]*3,' ',d[13][2]*3,' ',d[14][2]*3,' ',vb,"STAR 1",hb*32,vb)
    print(vb," "*50,vb,d[0][2]*3,' ',d[1][2]*3,' ',red_path[0][0]*3,' ',red_path[0][1]*3,' ',d[4][2]*3,' ',d[5][2]*3,' ',common_path[9]*3,' ',green_path[2]*3,' ',common_path[15]*3,' ',d[9][2]*3,' ',d[10][2]*3,' ',green_path[0][0]*3,' ',green_path[0][1]*3,' ',d[13][2]*3,' ',d[14][2]*3,' ',vb,"0 "*16," "*6,vb)
    print(vb," "*50,vb,d[0][3]*3,' ',d[1][3]*3,' ',red_path[0][3]*3,' ',red_path[0][2]*3,' ',d[4][3]*3,' ',d[5][3]*3,' ',common_path[8]*3,' ',green_path[3]*3,' ',common_path[16]*3,' ',d[9][3]*3,' ',d[10][3]*3,' ',green_path[0][3]*3,' ',green_path[0][2]*3,' ',d[13][3]*3,' ',d[14][3]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][3]*3,' ',d[1][3]*3,' ',red_path[0][3]*3,' ',red_path[0][2]*3,' ',d[4][3]*3,' ',d[5][3]*3,' ',common_path[8]*3,' ',green_path[3]*3,' ',common_path[16]*3,' ',d[9][3]*3,' ',d[10][3]*3,' ',green_path[0][3]*3,' ',green_path[0][2]*3,' ',d[13][3]*3,' ',d[14][3]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][4]*3,' ',d[1][4]*3,' ',d[2][4]*3,' ',d[3][4]*3,' ',d[4][4]*3,' ',d[5][4]*3,' ',common_path[7]*3,' ',green_path[4]*3,' ',common_path[17]*3,' ',d[9][4]*3,' ',d[10][4]*3,' ',d[11][4]*3,' ',d[12][4]*3,' ',d[13][4]*3,' ',d[14][4]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][4]*3,' ',d[1][4]*3,' ',d[2][4]*3,' ',d[3][4]*3,' ',d[4][4]*3,' ',d[5][4]*3,' ',common_path[7]*3,' ',green_path[4]*3,' ',common_path[17]*3,' ',d[9][4]*3,' ',d[10][4]*3,' ',d[11][4]*3,' ',d[12][4]*3,' ',d[13][4]*3,' ',d[14][4]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][5]*3,' ',d[1][5]*3,' ',d[2][5]*3,' ',d[3][5]*3,' ',d[4][5]*3,' ',d[5][5]*3,' ',common_path[6]*3,' ',green_path[5]*3,' ',common_path[18]*3,' ',d[9][5]*3,' ',d[10][5]*3,' ',d[11][5]*3,' ',d[12][5]*3,' ',d[13][5]*3,' ',d[14][5]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][5]*3,' ',d[1][5]*3,' ',d[2][5]*3,' ',d[3][5]*3,' ',d[4][5]*3,' ',d[5][5]*3,' ',common_path[6]*3,' ',green_path[5]*3,' ',common_path[18]*3,' ',d[9][5]*3,' ',d[10][5]*3,' ',d[11][5]*3,' ',d[12][5]*3,' ',d[13][5]*3,' ',d[14][5]*3,' ',vb," "*39,vb)
    print(vb,Fore.RED+"RED STAR",hb*41,vb,common_path[0]*3,' ',common_path[1]*3,' ',common_path[2]*3,' ',common_path[3]*3,' ',common_path[4]*3,' ',common_path[5]*3,' ',d[6][6]*3,' ',green_path[6]*3,' ',d[8][6]*3,' ',common_path[19]*3,' ',common_path[20]*3,' ',common_path[21]*3,' ',common_path[22]*3,' ',common_path[23]*3,' ',common_path[24]*3,' ',vb,"STAR 2",hb*32,vb)
    print(vb,"0 "*16," "*17,vb,common_path[0]*3,' ',common_path[1]*3,' ',common_path[2]*3,' ',common_path[3]*3,' ',common_path[4]*3,' ',common_path[5]*3,' ',d[6][6]*3,' ',green_path[6]*3,' ',d[8][6]*3,' ',common_path[19]*3,' ',common_path[20]*3,' ',common_path[21]*3,' ',common_path[22]*3,' ',common_path[23]*3,' ',common_path[24]*3,' ',vb,"0 "*16," "*6,vb)
    print(vb," "*50,vb,common_path[51]*3,' ',red_path[1]*3,' ',red_path[2]*3,' ',red_path[3]*3,' ',red_path[4]*3,' ',red_path[5]*3,' ',red_path[6]*3,' ',d[7][7]*3,' ',yellow_path[6]*3,' ',yellow_path[5]*3,' ',yellow_path[4]*3,' ',yellow_path[3]*3,' ',yellow_path[2]*3,' ',yellow_path[1]*3,' ',common_path[25]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,common_path[51]*3,' ',red_path[1]*3,' ',red_path[2]*3,' ',red_path[3]*3,' ',red_path[4]*3,' ',red_path[5]*3,' ',red_path[6]*3,' ',d[7][7]*3,' ',yellow_path[6]*3,' ',yellow_path[5]*3,' ',yellow_path[4]*3,' ',yellow_path[3]*3,' ',yellow_path[2]*3,' ',yellow_path[1]*3,' ',common_path[25]*3,' ',vb," "*39,vb)
    print(vb,Fore.YELLOW+"YELLOW STAR",hb*38,vb,common_path[50]*3,' ',common_path[49]*3,' ',common_path[48]*3,' ',common_path[47]*3,' ',common_path[46]*3,' ',common_path[45]*3,' ',d[6][8]*3,' ',blue_path[6]*3,' ',d[8][8]*3,' ',common_path[31]*3,' ',common_path[30]*3,' ',common_path[29]*3,' ',common_path[28]*3,' ',common_path[27]*3,' ',common_path[26]*3,' ',vb,"STAR 3",hb*32,vb)
    print(vb,"0 "*16," "*17,vb,common_path[50]*3,' ',common_path[49]*3,' ',common_path[48]*3,' ',common_path[47]*3,' ',common_path[46]*3,' ',common_path[45]*3,' ',d[6][8]*3,' ',blue_path[6]*3,' ',d[8][8]*3,' ',common_path[31]*3,' ',common_path[30]*3,' ',common_path[29]*3,' ',common_path[28]*3,' ',common_path[27]*3,' ',common_path[26]*3,' ',vb,"0 "*16," "*6,vb)
    print(vb," "*50,vb,d[0][9]*3,' ',d[1][9]*3,' ',d[2][9]*3,' ',d[3][9]*3,' ',d[4][9]*3,' ',d[5][9]*3,' ',common_path[44]*3,' ',blue_path[5]*3,' ',common_path[32]*3,' ',d[9][9]*3,' ',d[10][9]*3,' ',d[11][9]*3,' ',d[12][9]*3,' ',d[13][9]*3,' ',d[14][9]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][9]*3,' ',d[1][9]*3,' ',d[2][9]*3,' ',d[3][9]*3,' ',d[4][9]*3,' ',d[5][9]*3,' ',common_path[44]*3,' ',blue_path[5]*3,' ',common_path[32]*3,' ',d[9][9]*3,' ',d[10][9]*3,' ',d[11][9]*3,' ',d[12][9]*3,' ',d[13][9]*3,' ',d[14][9]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][10]*3,' ',d[1][10]*3,' ',d[2][10]*3,' ',d[3][10]*3,' ',d[4][10]*3,' ',d[5][10]*3,' ',common_path[43]*3,' ',blue_path[4]*3,' ',common_path[33]*3,' ',d[9][10]*3,' ',d[10][10]*3,' ',d[11][10]*3,' ',d[12][10]*3,' ',d[13][10]*3,' ',d[14][10]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][10]*3,' ',d[1][10]*3,' ',d[2][10]*3,' ',d[3][10]*3,' ',d[4][10]*3,' ',d[5][10]*3,' ',common_path[43]*3,' ',blue_path[4]*3,' ',common_path[33]*3,' ',d[9][10]*3,' ',d[10][10]*3,' ',d[11][10]*3,' ',d[12][10]*3,' ',d[13][10]*3,' ',d[14][10]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][11]*3,' ',d[1][11]*3,' ',blue_path[0][0]*3,' ',blue_path[0][1]*3,' ',d[4][11]*3,' ',d[5][11]*3,' ',common_path[42]*3,' ',blue_path[3]*3,' ',common_path[34]*3,' ',d[9][11]*3,' ',d[10][11]*3,' ',yellow_path[0][0]*3,' ',yellow_path[0][1]*3,' ',d[13][11]*3,' ',d[14][11]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][11]*3,' ',d[1][11]*3,' ',blue_path[0][0]*3,' ',blue_path[0][1]*3,' ',d[4][11]*3,' ',d[5][11]*3,' ',common_path[42]*3,' ',blue_path[3]*3,' ',common_path[34]*3,' ',d[9][11]*3,' ',d[10][11]*3,' ',yellow_path[0][0]*3,' ',yellow_path[0][1]*3,' ',d[13][11]*3,' ',d[14][11]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][12]*3,' ',d[1][12]*3,' ',blue_path[0][2]*3,' ',blue_path[0][3]*3,' ',d[4][12]*3,' ',d[5][12]*3,' ',common_path[41]*3,' ',blue_path[2]*3,' ',common_path[35]*3,' ',d[9][12]*3,' ',d[10][12]*3,' ',yellow_path[0][3]*3,' ',yellow_path[0][2]*3,' ',d[13][12]*3,' ',d[14][12]*3,' ',vb,"STAR 4",hb*32,vb)
    print(vb," "*50,vb,d[0][12]*3,' ',d[1][12]*3,' ',blue_path[0][2]*3,' ',blue_path[0][3]*3,' ',d[4][12]*3,' ',d[5][12]*3,' ',common_path[41]*3,' ',blue_path[2]*3,' ',common_path[35]*3,' ',d[9][12]*3,' ',d[10][12]*3,' ',yellow_path[0][3]*3,' ',yellow_path[0][2]*3,' ',d[13][12]*3,' ',d[14][12]*3,' ',vb,"0 "*16," "*6,vb)
    print(vb,Fore.BLUE+"BLUE STAR",hb*40,vb,d[0][13]*3,' ',d[1][13]*3,' ',d[2][13]*3,' ',d[3][13]*3,' ',d[4][13]*3,' ',d[5][13]*3,' ',common_path[40]*3,' ',blue_path[1]*3,' ',common_path[36]*3,' ',d[9][13]*3,' ',d[10][13]*3,' ',d[11][13]*3,' ',d[12][13]*3,' ',d[13][13]*3,' ',d[14][13]*3,' ',vb," "*39,vb)
    print(vb,"0 "*16," "*17,vb,d[0][13]*3,' ',d[1][13]*3,' ',d[2][13]*3,' ',d[3][13]*3,' ',d[4][13]*3,' ',d[5][13]*3,' ',common_path[40]*3,' ',blue_path[1]*3,' ',common_path[36]*3,' ',d[9][13]*3,' ',d[10][13]*3,' ',d[11][13]*3,' ',d[12][13]*3,' ',d[13][13]*3,' ',d[14][13]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][14]*3,' ',d[1][14]*3,' ',d[2][14]*3,' ',d[3][14]*3,' ',d[4][14]*3,' ',d[5][14]*3,' ',common_path[39]*3,' ',common_path[38]*3,' ',common_path[37]*3,' ',d[9][14]*3,' ',d[10][14]*3,' ',d[11][14]*3,' ',d[12][14]*3,' ',d[13][14]*3,' ',d[14][14]*3,' ',vb," "*39,vb)
    print(vb," "*50,vb,d[0][14]*3,' ',d[1][14]*3,' ',d[2][14]*3,' ',d[3][14]*3,' ',d[4][14]*3,' ',d[5][14]*3,' ',common_path[39]*3,' ',common_path[38]*3,' ',common_path[37]*3,' ',d[9][14]*3,' ',d[10][14]*3,' ',d[11][14]*3,' ',d[12][14]*3,' ',d[13][14]*3,' ',d[14][14]*3,' ',vb," "*39,vb)
    print(hb*188)
turn()
