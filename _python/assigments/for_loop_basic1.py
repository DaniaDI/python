# q1
for i in range(151):
    print(i)

# q2
for i in range(5, 1001):
    if (i % 5 == 0):
        print(i)
        
# q3
for i in range(1, 101):
    if(i % 10 == 0):
        print("Coding Dojo")
    elif(i % 5 == 0):
        print("Coding")

# q4
sum = 0
for i in range(0, 500001):
    if(i % 2 != 0) :
        sum+=i
print(sum)

# q5
for i in range(2018 ,0,-4):
    if(i % 2 == 0):
        print(i)


lowNum = 2 
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if(i % mult == 0):
        print(i)