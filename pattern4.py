n=int(input())
space=0
for row in range(n):
    for j in range(space):
        print(" ",end="")
    for star in range(n):
        print("*",end="")
    space=space+1
    print()
    
