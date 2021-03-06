# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(a, b):
    return (a + b)
print("f1:", f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(num1, *args):
    total = num1
    for num in args:
        total = total + num
    return total
# ? assumes at least one number, assigns it to total (Similar to current value in js reduce()). If additional *args/arguments/numbers exist, loop through and add to 'total'.

print("f2, should be 1:", f2(1))                   # Should print 1
print("f2, should be 4:",f2(1, 3))                 # Should print 4
print("f2: should be -7",f2(1, 4, -12))            # Should print -7
print("f2 should be 33:",f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print("f2 should be 22:",f2(sum(a)))   # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(x, y = 1):
    return (x + y)

print("f3 should be 3:", f3(1, 2))  # Should print 3
print("f3 should be 9:", f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(**kwargs):
    for key, value in kwargs.items(): 
        print ("key: %s, value: %s" %(key, value)) 
# ? loops through kwargs parameters for key, value, print line is just like what we did in 04_printing.py

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)
# ? difference is that the hp value is an integer and not a string, need ** to access/spread the kwargs to display the int