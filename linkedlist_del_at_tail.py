class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        




def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head





def printlist(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
    
    
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)


    
def deltailnode(head):
    curr=head
    prv=None
    while curr.next!=None:
        prv=curr
        curr=curr.next
    prv.next=None
    return head

head=deltailnode(head)
printlist(head)

    

    
