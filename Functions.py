#Functions
def hello(name): #Name the function so ppl know what is going on
    print('Hello '+ name)
    
hello('Bartek') #Activetes the function
hello('Tom')

def hello(name = 'my friend'): #Can call function without putting name
    print('Hello '+ name)
    
hello('Bartek') #Activetes the function
hello('Tom')
hello()

def hello(name, age):
    print('Hello ' + name + ' you are ' + str(age) + ' years old!')
    
hello('Bartek', 26)
hello('Tom', 15)

def change(value):
    value = 2 #This is not doing insid of function
    
val = {'name': 'Bartek'}
change(val)

print(val)

def hello2(name):
    if not name:
        return
    print('Hello ' + name)
    
hello2('Bartek')

def hello3(name):
    print('Hello ' + name)
    return name, 'Sebastian', 9
    
print(hello3('Bartek'))

#Variable Scope, local vs global, local is inside of function, global in anywhere.

age = 8 #Visible for any code before any function, so it can be used everywhere

def test():
    print(age)
    
test()

#Nested Functions
def talk(phrase):
    def say(word): #This is function inside of function
        print(word)
        
    words = phrase.split(' ')
    for word in words:
        say(word)
        
talk('I am going to the store')

def count():
    count = 0
    
    def increment():
        nonlocal count #Refers to the varible in previous function (nonlocal)
        count = count + 1
        print(count)
        
    increment()
    
count()