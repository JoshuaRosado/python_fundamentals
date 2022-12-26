# #Output ("Hello World")
print("Hello World")

# # Output ("Hello Noelle!")
name = "Joshua"
print("Hello " + name + "!") # with +
print("Hello",name,"!") # with comma

# 3. print "Hello 42!" with the number in a variable
num = 67
print("Hello", num,"!")	# with a comma
print("Hello " + str(num) +"!")	#NINJA BONUS # with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
food_1 = "pizza"
food_2 = "spaghetti"
print("I love to eat {} and {}.".format(food_1, food_2)) # with .format()


print (f"I love to eat {food_1} and {food_2}.")# print( your code here ) # with an f string
