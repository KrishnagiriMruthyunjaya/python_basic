word=input()
print(word)
store=dict()

for ch in word:
    if ch in store:
        store[ch]=store[ch]+1
    else:
        store[ch]=1
print(store)

resultchar='#'
resultfeq=0
all=store.keys()
for ele in all:
    if store[ele]>resultfeq:
        resultfeq=resultfeq+1
        resultchar=ele
print(resultchar,resultfeq)

