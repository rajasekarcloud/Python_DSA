# Print increasing triangle of stars
# *
# * *
# * * *
# * * * *
# * * * * *
def increase_star(n):
    for row in range(n):
        for column in range(row+1):
            print("*",end=" ");
        print("\n")
increase_star(5);
