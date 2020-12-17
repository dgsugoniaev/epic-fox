# What will the following code output?

def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3        # When square is called, x is bound to the parameter value that is passed in, 2.

print(h(2))                     # 7

# ________________________________________________________________________________________________________________

# What will the following code output?

def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print(g(h(2))                   # 10

# ✔️ h(2) returns 7, so y is bound to 7 when g is invoked.

