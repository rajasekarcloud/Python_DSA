# Print row of stars
# * * * *
# * * * *
# * * * *
def rowstar(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("\n")

rowstar(3);
