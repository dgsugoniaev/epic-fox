# What does this function print?

def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)             # 25

# Explanation: ✔️ The function square returns the square of its input (via a call to pow).
