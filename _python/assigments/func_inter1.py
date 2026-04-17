import random
def randInt(min= 0 , max= 100):
    num = int(random.random() * (max - min) + min)
    return num
   
print(randInt())
print(int(randInt(max=50)))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=10, max=35)) 
print(round(randInt()))

