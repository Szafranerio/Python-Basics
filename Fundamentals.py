#Variable can be strings, int, etc
name = 'Bartek' #String
age = 39  #Int

print(name) #Print Bartek
name += ' is my name'
print(name) #Updated version prints Bartek is my name

#String methods
print(name.upper()) #Put . and check what you need remember about ()
print(len(name)) #Check the length
print('a' in name) #Check if smth is in the string
print(name[1]) #Gives a specific letter from the name var. It counts from zero
print(name[-2]) #Starts from the back
print(name[1:3]) 
print(name[:5]) #From zero index until the 5th
type(age) #Shows the type of data, in this case it shows int for the number

#Arithmetic Operators

age += 4 #Add four to 39
print(age)

age *=3241 #Multiply it by chosne number
print(age)

a = 1
b = 2 

print(a == b) #False
print( a < b) #True
print(a != b) #True (is different)
print (a > b) #False 

print(abs(-5.5)) #Result is 5.5
print(round(5.43213)) #Rounds the number
print(round(4.4312413, 1)) #One decimal point, bigger number more after dot

#Input()
name = input('What is your name: ')
print('Your name is ' + name)

#Control statments

condition = False

if condition == True:
    print('The condition')
    print('was true')
    
else: 
    print('The condition')
    print('was false')

