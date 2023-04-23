# Print decreasing triangle of stars
# * * * * *
# * * * *
# * * *
# * *
# *

def reversed_triangle(n):
    for row in reversed(range(n+1)):
        for column in range(row):
            print("*",end=" ");
        print("\n");

reversed_triangle(5);
