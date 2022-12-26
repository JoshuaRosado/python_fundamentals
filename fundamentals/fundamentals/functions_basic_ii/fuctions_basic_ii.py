# ! Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    output = []
    for i in range(num,-1 , -1):
        output.append(i)
    return output 

print(countdown(13))

#PRINT [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_return(my_list):
    print(my_list[0])
    print(my_list[1])
    
print(print_return([1, 2]))

# PRINT 1,2, None

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(my_list):
    return my_list[0] + len(my_list)

print(first_plus_length([10,20,30,40,50]))

#PRINT 15

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def value_greater_than_second(my_list):
    if len (my_list) < 2:
        return False
    output = []
    for i in range(0,len(my_list)):
        if my_list[i] > my_list[1]:
            output.append(my_list[i])
    print(len(output))
    return output

print(value_greater_than_second([5,2,3,2,1,4]))
print(value_greater_than_second([3]))

#PRINT 3
# [5, 3, 4]
# False


#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_value(size, value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_value(3,10))
print(length_value(1,100))

# #PRINT [10, 10, 10]
# [100]