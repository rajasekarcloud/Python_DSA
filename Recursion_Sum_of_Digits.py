# Sum of digits
# Eg: 54 -> 5 + 4 = 9
# We use % and /
# print (10/5); Answer: 2
# print (10%5); Answer: 0
def sumofdigits(n):
    assert n>=0 and int(n) == n, "The number has to be positive integer only"
    if n == 0:
        return 0;
    else:
        return int(n%10) + sumofdigits(int(n/10))
print(sumofdigits(53));