# Function Composition _______________________________________________________

# Write two functions, one called addit and one called mult.
# addit takes one number as an input and adds 5.
# mult takes one number as an input, and multiplies that input by whatever
# is returned by addit, and then returns the result.

def addit(x):
    y = x + 5
    return y

def mult(x):
    z = x * addit(x)
    return z

x = 3
print(addit(3))
print(mult(3))

# Explanation: Because x is not defined as a local variable in either function,
# both functions search for x in the global stack.
