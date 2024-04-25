#Lists
dogs = ['Roger', 'Azor', 'Ozi']

print('Roger' in dogs) #Check if the item is in the list
print(dogs[0]) #Print the item in the list based on its index
print(dogs[2])
print(dogs[-1])

dogs[2] = 'Bartek' #Updates the list with different name based on index
print(dogs)

print(dogs[:2]) #SLice the list from zero index to second index
print(dogs[1:3]) #THe inside of the list
print(dogs[2:]) #Prints from second index to the end of the list

dogs.append('Judah') #Adds an item to the list
print(dogs)

dogs.remove(dogs[0]) #Removes an item from the list based on index
print(dogs)

print(dogs) 

items = ['Desk', 'Table', 'Chair', 'Mirror', 'cupboard', 'Armchair']

items.sort() #Sorts the list
print(items)

print(sorted(items, key=str.lower))
print(items)

#Tuples, once created cannot be modified!!!
names = ('Roger', 'Sebastian', 'Maciej')

print(names[0])
print(len(names))
print('Roger' in names)
print(names [0:2])
print(sorted(names))

#Dictionaries key and values
dog = {'name': 'Roger', 'age': 7}
print(dog['name']) 

dog['name'] = 'Ozi'
print(dog['name'])
print('color' in dog)
print(dog.keys()) #Prints all keys in the dic
print(dog.values()) #Returns values only

dog['food'] = 'Meat'
print(dog)

del dog['age']
print(dog)

#Sets, can only have uniqye items in the set!!! No two same values
set1 = {'Roger', 'Sebastian'}
set2 = {'Roger'}

intersect = set1 & set2
print(intersect)

difference = set1 - set2
print(difference)

print(list(set1)) #Changes to set