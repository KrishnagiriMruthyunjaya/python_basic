n=int(input()) 
space=n-1
count=1
for i in range(n):
    for j in range(space):
         print(" ",end="")
    for j in range(count):
        print(j+1,end="")
    print()
    space=space-1
    count=count+2
