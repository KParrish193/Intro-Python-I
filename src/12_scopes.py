# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
# ? is global
x = 12

def change_x():
    global x
    # ? ^declare x as global
    x = 99
    # ? ^this modifies x

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)

# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()

# ? Nonlocal variable are used in nested function whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.