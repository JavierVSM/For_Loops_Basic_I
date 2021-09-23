print ("=========== Task 1 ===========")

#Basic - Print all integers from 0 to 150.
for basic in range (0,151):
    print (basic)

print ("=========== Task 2 ===========")

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for fiveMultiples in range (5,1001,5):
     print (fiveMultiples)

print ("=========== Task 3 ===========")

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for countDojo in range (1,101):
    if countDojo%5 == 0 and countDojo%10 != 0:
        print ("Coding")
    if countDojo%10 == 0:
        print ("Coding Dojo")
    else:
        print (countDojo)

print ("=========== Task 4 ===========")

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

num=0

for addOdd in range (2,500000,2):
    num= num + addOdd

finalNum = num
print (finalNum)

print ("=========== Task 5 ===========")

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for countdown in range (2018,0,-4):
    print (countdown)

print ("=========== Task 6 ===========")

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)    
lowNum= 2
highNum= 9
mult= 3
limit= highNum+1 

for flexCount in range (lowNum, limit):
    if flexCount%mult == 0:
        print (flexCount)
