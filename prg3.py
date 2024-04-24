#Write a python program to accept a list of
    #integers and print total count of negative
   # numbers in the list 
 
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele < 0:
        result = result + 1 
print(result)
