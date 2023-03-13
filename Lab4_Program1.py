# Program Name: Lab4_Program1.py
# Course: IT3883/Section W01
# Student Name: Trevor Harbin
# Assignment Number: Lab4
# Due Date: 03/13/2023
# Purpose: Create a file with the information that was collected about dogs.
dogs =[]
#dogs=[('Sulley','Bud','8','175','Great Dane'),('Jack','Drake','5','15','Chihuahua'),('Luna','Rita','3','120','English Mastiff'),('Dakota','Mario','4','20','Sheltie'),('Elwood','Jim','6','90','German Shephard')]

for i in range(1,6):
    name = input(f"Input Dog {i}'s name: ")
    lname = input(f"Input the Owner's Last name: ")
    age = input(f"Input {name}'s age: ")
    weight = input(f"Input {name}'s weight (lbs): ")
    breed = input(f"Input {name}'s Breed: ")
    dogs.append((name,lname,age,weight,breed))

#Loop 5 times and collect information about the dogs

f = open("tharbin.txt","w")
f.write(str(dogs))


print(f"[Process Completed: File \"{f.name}\" written to]")

#Creates a file and writes the array into it. In Hindsight, I should have written all the data per line so I can write it into an array easier in the next file.
#Too late to change it as I am writing this #yolo

f.close()