# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def odd_or_even(x):
    if x % 2 == 0:
        print("Even!")
    else:
        print("Odd")


odd_or_even(num)
