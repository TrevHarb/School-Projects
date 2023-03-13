# Program Name: Lab2.py
# Course: IT3883/Section W01
# Student Name: Trevor Harbin
# Assignment Number: Lab2
# Due Date: 02/06/2023
# Purpose: Prompts the USer for information about 6 dogs, then determines the cost of sheltering them based on weight class

dawgs=[]
#dawgs=[(49, 4, 2, 2), (19, 9, 3, 1), (108, 7, 1, 4), (135, 6, 23, 4)]
counter=1
while len(dawgs)<4:
    weight=int(input('Input Weight of Dog '+str(counter)+' (Lb): '))
    dlen =int(input('Days using our boarding service: '))
    hlen =int(input('Hours using our boarding service: '))
    category=0
    if weight<=19:
        category=1
    elif weight<=49:
        category=2
    elif weight<=99:
        category=3
    else:
        category=4
    
    dawgs.append((weight, dlen, hlen, category))
    counter+=1

counter=1

for i in dawgs:
    cost=0
    week=0
    if i[1]>6:
        week = i[1]//7
        dlen=i[1]%7
    else:
        dlen=i[1]
    match i[3]:
        case 1:
            drate=30
            hrate=8
            wrate=150
        case 2:
            drate=35
            hrate=9
            wrate=160
        case 3:
            drate=40
            hrate=10
            wrate=175
        case 4:
            drate=45
            hrate=12
            wrate=200
        case default:
            drate=0
            hrate=0
            wrate=0
    cost= drate*dlen+hrate*i[2]+wrate*week
    print('Cost for Dog '+str(counter)+": $"+str(cost))
    counter+=1