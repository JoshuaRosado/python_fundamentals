num1 = 42  #variable declaration, number initialized
num2 = 2.3 #variable declaration, decimal/float initialized
boolean = True #variable declaration, boolean initialized
string = 'Hello World' # variable declaration, string initialized


#variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalapenos', 'Cheese', 'Olives']

#variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

#variable declaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')

#print to console, type check
print(type(fruit))

#print to console, List access value
print(pizza_toppings[1])

#list add value
pizza_toppings.append('Mushrooms')

#print to console, Dictionary access value
print(person['name'])

#Dictionary change value
person['name'] = 'George'

#Dictionary change value
person['eye_color'] = 'blue'

#print to console, List access value
print(fruit[2])


# Conditional if, evaluation, print to console, Conditional else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")


# Conditional if --- elif --- else, print to console
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


#Loop starts at 0, goes up to until 5
for x in range(5):
    print(x)

#Loop starts at 2, goes up to until 5
for x in range(2,5):
    print(x)

#Loop starts at 2, goes up to until 10, increments by 3
for x in range(2,10,3):
    print(x)


#While loop, variable declaration
x = 0
while(x < 5):
    #printing to console
    print(x)
    #incrementing by x
    x += 1

# List delete value at the end
pizza_toppings.pop()
#List delete value at index(drawer # 1)
pizza_toppings.pop(1)

#print to console of Dictionary
print(person)
#Dictionary delete value
person.pop('eye_color')
#print to console of Dictionary
print(person)


#For loop through a list
for topping in pizza_toppings:
#Conditional if
    if topping == 'Pepperoni':
#Continue
        continue
    print('After 1st if statement')
#Conditional if
    if topping == 'Olives':
#Stops the loop
        break

#function declaration
def print_hello_ten_times():
#for loop starts at 0 up until to 10
    for num in range(10):
# print to console
        print('Hello')

#function call
print_hello_ten_times()

#function declaration with PARAMETER x
def print_hello_x_times(x):
# for loop starts at 0 up until a given number x
    for num in range(x):
# print to console
        print('Hello')

#function call
print_hello_x_times(4)

#function declaration with default PARAMETER
def print_hello_x_or_ten_times(x = 10):
# for loop starts at 0 up until a given number x
    for num in range(x):
#print to console
        print('Hello')
        

#function call goes to 10
print_hello_x_or_ten_times()
# function call goes to 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
#print to console variable(NO VALUE)
print(num3)
#give a variable a value
num3 = 72
#TUPLE CAN NOT BE CHANGED
fruit[0] = 'cranberry'
#print to console 
print(person['favorite_team'])
#print to console access to list(INDEX NOT FOUND)
print(pizza_toppings[7])
#print to console boolean
print(boolean)
# add value to TUPLE (ERROR!)
fruit.append('raspberry')
# delete value at index (ERROR!)
fruit.pop(1)