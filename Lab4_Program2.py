# Program Name: Lab4_Program2.py
# Course: IT3883/Section W01
# Student Name: Trevor Harbin
# Assignment Number: Lab4
# Due Date: 03/13/2023
# Purpose: Read file about dogs and calculate the dosage of medication with that information.


l=open("tharbin.txt",'r')
if l.readable():
    doggos=l.read()
l.close()

#Open file and read information about dogs.
#This data is in a list format but in a string, Converting this sucked

doggos="T"+doggos
foo=doggos.split(")")

#I had to add a buffer character to make all the splits the same length at beginning and end.

foo.pop()

#After splitting, there was an extra empty cell at the end, so I popped it so only my data is in the list.

data=[]


for i in foo:
    i=i[3:].split(',')
    for s in i:
        s=s[1:].strip("'")
        data.append(s)

#Split and strip all the extraneous characters from the data so that data is a list with just the values of the data. 


dosage=0
name=""


for i in range(3,26,5):
    weight=int(data[i])
    if weight<=77:
        if weight<=11:
            dosage=0.25
        elif weight<=22:
            dosage=.5
        elif weight<=33:
            dosage=0.75
        elif weight<=44:
            dosage=1.00
        elif weight<=55:
            dosage=1.25
        elif weight<=66:
            dosage=1.50
        else:
            dosage=1.75
    else:
        if weight>=133:
            dosage=3.50
        elif weight>=122:
            dosage=3.00
        elif weight>=111:
            dosage=2.75
        elif weight>=100:
            dosage=2.50
        elif weight>=89:
            dosage=2.25
        else:
            dosage=2.00

    #I split the elif statements in half for a fast run time. But all it is doing is checking what the weight is for the dog and setting the dosage to the correct value


    print(f"The Dosage for {data[i-3]}, {data[i-2]}'s {data[i-1]} Year old {data[i+1]}, is {dosage} ml.")

    #I then print out the information for the dogs using an fstring to input the values. 