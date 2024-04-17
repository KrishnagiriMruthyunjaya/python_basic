n=int(input())
space=n-1

for i in range(1,n+1):
    for j in range(space):
        print(" ",end="")
    for j in range(i):
        print(j+1,end="")
    print()
    space=space-1
    
