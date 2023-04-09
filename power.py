# Power of a number
# Input 2 and 3
# 2^3=8

def power(a,b):
    if b == 1:
        return a*b;
    else:
        return a * power(a,b-1);
print(power(2,3))
