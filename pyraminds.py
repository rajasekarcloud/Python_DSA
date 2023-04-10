# Printing one sided pyramids using recursion
# ******
# ****
# ***
# **
# *
def pyramid(n):
    if n == 0:
        return;
    else:
        print("*" * n); # Prints Pyramid bottom to up
        pyramid(n-1);
        print("*"*n); # Prints Pyramid up to bottom

pyramid(6);
