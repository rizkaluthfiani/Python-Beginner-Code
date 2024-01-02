# create a code that will print out "Fizz" if a number is able to be divided by 3, "Buzz" if able to be divided by 5, and "FizzBuzz" if able to be divided by 3 and 5.

for number in range(1, 101):
    # condition 1: check first if the number can be divided by 3 and 5. if this condition is true, then the program doesn't need to execute the next condition.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # condiiton 2: check if the number can be divided by 3 to print "Fizz". If this condition is placed first as the first condition, then if we check the number that can be divided by 3 and 5 such as 15, it will print "Fizz" instead of "FizzBuzz". Anyway, we can either create "Buzz" condition as the 2nd condition, it will do the same.
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    # if the number cannot be divided by 3, 5 or 3 & 5, print the number itself instead.
    else:
        print(number)