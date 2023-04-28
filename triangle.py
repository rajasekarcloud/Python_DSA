# Increasing/Decreasing triangle
def triangle(count):
    for row in (range(count+1)): # If I add reversed - Prints decreased triangle
        for col in range(row):
            print("*",end=" ");
        print("\n")

triangle(5);# 5 Rows
