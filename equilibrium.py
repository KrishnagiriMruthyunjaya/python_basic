1. Given a sequence arr[] of size n, Write a function int equilibrium(arr, n) that returns an equilibrium index (if any) or -1 if no equilibrium index exists. 
 
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. 


num=list(map(int,input().split()))
n=len(num)
result=-1
for i in range(n):
    leftsum=0
    for j in range(i+1):
        leftsum +=num[j]
    rightsum=0
    for j in range(i+1,n):
        rightsum +=num[j]
    if rightsum==leftsum:
        result=i
        break
print(result)
