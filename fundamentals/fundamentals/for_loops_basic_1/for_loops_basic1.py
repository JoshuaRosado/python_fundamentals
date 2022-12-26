# ===BASIC
for nums in range(0, 151):
    print(nums)  # PRINTS numbers 0-150


#===MULTIPLES BY FIVE(5)
for nums in range(5,1001, 5):
    print(nums) # PRINTS multiples of 5 from 5-1000 


#===COUNTING, THE DOJO WAY
for nums in range(0, 100):
    print(nums)
    if nums % 10 == 0:
        print("Coding Dojo")
    elif nums % 5 == 0:
        print("Coding")
else: 
    print(nums)


# ===WHOA, THAT SUCKER'S IS HUGE
total = 0 # total equals 0
for nums in range(1, 500001, 2): # start at 1, ends at 500,001(to get that last number printed, incrementing by 2 to get all the ODD NUMBERS)
    total += nums # Adding or Appending "total" that equals 0 to "nums" that has the final sum
print(total) # Now total has the final sum that is 62500000000

# ===COUNTDOWN BYE 4
for nums in range(2018, 0 , -4): #start at 2018, ends at 0 , decreasing by 4
    print(nums)

# ===FLEXIBLE COUNTER

lowNum = 10
highNum = 26
mult = 2

for nums in range(lowNum, highNum, 1): #start at lowNum, ends at highNum, increasing by one
    if nums % mult == 0: # if nums is divisible by mult(2) and equals 0 
        print(nums)

