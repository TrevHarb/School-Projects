# Program Name: Lab1.py
# Course: IT3883/Section W01
# Student Name: Trevor Harbin
# Assignment Number: Lab1
# Due Date: 01/23/ 2023
# Purpose: Prompts User for name and 5 numbers and then prints out after calculating Sum, difference, and average


def sumnum(nums):
    sum=0
    for i in nums:
        sum+=i
    return 'Sum: '+str(sum)
def prodnum(nums):
    prod=1
    for i in nums:
        prod*=i
    return 'Product: ' + str(prod)
def avgnum(nums):
    avg=0
    for i in nums:
        avg+=i
    return 'Average: ' +str(avg/len(nums))
def minnum(nums):
    min = nums[0]
    for i in nums:
        if i<min:
            min = i
    return 'Minimum: ' + str(min)
    
    
name = input('What is your name: ')
print('My name is '+name)

print('Please enter 5 numbers')
nums = []
for i in range(0,5):
    temp=int(input('Number '+str(i+1)+': '))
    nums.append(temp)
print(sumnum(nums))
print(prodnum(nums))
print(avgnum(nums))
print(minnum(nums))

