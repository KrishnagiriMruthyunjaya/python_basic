n=int(input())
space=0
star=n
for row in range(n):
    for j in range(space):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    space=space+1
    star=star-1
    print()
