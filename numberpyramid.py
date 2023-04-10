# Print number pyramids
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
def numpyramid(n):
    for i in range(1,n+1):
        for x in range(1,i):
            print(x,end="\t")
        print("\n")
numpyramid(5);

