# Program Name: Lab3.py
# Course: IT3883/Section W01
# Student Name: Trevor Harbin
# Assignment Number: Lab3
# Due Date: 02/20/2023
# Purpose: To calculate the average time for each event as well as who completed the Triathalon the fastest.
import math
competitors = []
#competitors = [('Amber', '0:59:03', '1:53:01', '0:33:24'), ('Stacey', '0:38:45', '1:26:04', '0:32:37'), ('Lizzy', '0:45:23', '1:23:34', '0:35:55'), ('Erin', '0:35:36', '1:34:22', '0:34:31')]
for i in range(0,4):
    name = str(input("Input name of competitor: "))
    running = str(input("Input the fastest Running Time (Format: h:mm:ss): "))
    biking = str(input("Input the fastest Biking Time (Format: h:mm:ss): "))
    swimming = str(input("Input the fastest Swimming Time (Format: h:mm:ss): "))
    competitors.append((name,running,biking,swimming))

def information(competitors):
    temp=""
    for i in competitors:
        temp+="\n------------------------"
        temp+="\nName: "+i[0]
        temp+="\nRunning Time: "+i[1]
        temp+="\nBiking Time: "+i[2]
        temp+="\nSwimming Time: "+i[3]
    temp+="\n------------------------"
    return temp
def average(competitors, event):
    temp="Average time for "
    match event:
        case 1:
            temp+="Running: "

            splits=[]
            for i in competitors:
                splits.append(i[1].split(":"))
            #Creates an array for each swimming time (Hr, Min, Sec) and puts that array into a list

            comptimes=[]
            for i in splits:
                comptimes.append((int(i[0])*3600)+(int(i[1])*60)+(int(i[2])))
            #Adds the seconds, Minutes, and hours together to get the total time in seconds for each competitor            

            avg=sum(comptimes)/4
            t=(avg%60)
            min=((avg-t)/60)
            r=min%60
            hr=int((min-r)/60)
            #Takes the Average and converts it back to the previously used format

            if int(t) < int(t+0.5):
                t=math.ceil(t)
            #Used to round the number up if it is bigger than .5 as using int() will always truncate the number even if it is .99

            t=str(t)
            r=str(int(r))
            if len(r)<2:
                r="0"+r
            if len(t)<2:
                t="0"+t
            temp+=f'{hr}:{r}:{t}'
        case 2:
            temp+="Biking: "

            splits=[]
            for i in competitors:
                splits.append(i[2].split(":"))
            #Creates an array for each Biking time (Hr, Min, Sec) and puts that array into a list

            comptimes=[]
            for i in splits:
                comptimes.append((int(i[0])*3600)+(int(i[1])*60)+(int(i[2])))
            #Adds the seconds, Minutes, and hours together to get the total time in seconds for each competitor            

            avg=sum(comptimes)/4
            t=(avg%60)
            min=((avg-t)/60)
            r=min%60
            hr=int((min-r)/60)
            #Takes the Average and converts it back to the previously used format

            if int(t) < int(t+0.5):
                t=math.ceil(t)
            #Used to round the number up if it is bigger than .5 as using int() will always truncate the number even if it is .99

            t=str(int(t))
            r=str(int(r))
            if len(r)<2:
                r="0"+r
            if len(t)<2:
                t="0"+t
            temp+=f'{hr}:{r}:{t}'
        case 3:
            temp+="Swimming: "

            splits=[]
            for i in competitors:
                splits.append(i[3].split(":"))
            #Creates an array for each swimming time (Hr, Min, Sec) and puts that array into a list

            comptimes=[]
            for i in splits:
                comptimes.append((int(i[0])*3600)+(int(i[1])*60)+(int(i[2])))
            #Adds the seconds, Minutes, and hours together to get the total time in seconds for each competitor            

            avg=sum(comptimes)/4
            t=(avg%60)
            min=((avg-t)/60)
            r=min%60
            hr=int((min-r)/60)
            #Takes the Average and converts it back to the previously used format

            if int(t) < int(t+0.5):
                t=math.ceil(t)
            #Used to round the number up if it is bigger than .5 as using int() will always truncate the number even if it is .99

            t=str(t)
            r=str(int(r))
            if len(r)<2:
                r="0"+r
            if len(t)<2:
                t="0"+t
            temp+=f'{hr}:{r}:{t}'
    return temp
def fastest(competitors):
    temp="\nThe Winner is "
    ttime=[]
    itimes=[]

    for i in competitors:
        for l in range(1,4):
            itimes.append(i[l].split(':'))
        
        #Splits up times into Hr, Min, Sec and adds to list in order of competitors

        event=[]
        for s in itimes:
            event.append((int(s[0])*3600)+(int(s[1])*60)+(int(s[2])))
        ttime.append(sum(event))
        itimes.clear()
    
    #Calculates the time of each event in seconds and adds to list, which get added to gether and added to ttime. Does this per competitor so ttime is a list of total time, one per competitor in original order

    ftime = ttime[0]
    count=0
    win=0
    for j in ttime:
        if j<ftime:
            win=count
            ftime=j
        count+=1

    #Finds the fastest time as well as which person owns that time. 

    t=(ftime%60)
    min=((ftime-t)/60)
    r=min%60
    hr=int((min-r)/60)

    if int(t) < int(t+0.5):
        t=math.ceil(t)
            #Used to round the number up if it is bigger than .5 as using int() will always truncate the number even if it is .99

    t=str(t)
    r=str(int(r))
    if len(r)<2:
        r="0"+r
    if len(t)<2:
        t="0"+t

    temp+=f"{competitors[win][0]} with a total time of {hr}:{r}:{t}!"
    return temp

print(information(competitors))
print(average(competitors, 1))
print(average(competitors, 2))
print(average(competitors, 3))
print(fastest(competitors))