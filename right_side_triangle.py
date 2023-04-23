# Print right sided triangle
#       *
#     * *
#   * * *
# * * * *

def right_triangle(n):
    for row in range(n):
        for space in range(row,n):
            print("-",end=" ");
        for column in range(row+1):
            print("*",end=" ");
        print("\n");

right_triangle(3);
