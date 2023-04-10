# Printing array of stars
# Input as 4
# ****
# ****
# ****
# ****
def star(n):
    if n == 0:
        return;
    else:
        for i in range(n):
            print("*"*n);
star(3);
