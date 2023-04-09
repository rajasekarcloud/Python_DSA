# Factorial of a number using recursion
# 5 = 1*2*3*4*5
def factorial(n):
    if n == 1:
        return n;
    else:
        return n * factorial(n-1);

print(factorial(4));