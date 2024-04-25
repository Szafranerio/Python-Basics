#Loops

#While
condition = True 
while condition == True: #While this condition is true it will run the code constantly
    print('The condition is True')
    condition = False
    
count = 0 
while count < 10:
    print(count)
    count = count + 1 # or count += 1 
    
#For loops
items = [1, 2, 3, 4]
for item in items:
    print(item)
    
for item in range (15):
    print(item)

cities = ['Aalborg', 'Aarhus', 'Odense', 'Copenhagen']
for index, city in enumerate(cities):
    print(index, city)
    
#Break and continue 

items = [1,2,3,4,5,6,7,8,9]
for item in items:
    if item == 2: #Skips an chosen item
        continue #Keeps priting or anything else
    print(item)
    
for item in items:
    if item == 7:
        break #Break the loop
    print(item)