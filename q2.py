# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


six = ListNode(10)
five = ListNode(9,six)
four = ListNode(8,five)
three = ListNode(7,four)
two=ListNode(6,three)


head = ListNode(5)
head.next = two 
heads = head
  
class Solution:
    def removeNthFromEnd(self, head, n):
        current=head
        i=0
        values=[head.val]
        ## Traverse the list 
        while current.next!=None:
            i=i+1
            values.append(current.next.val)
            current = current.next
        
        print("Input linked list values : ",values)
        if i-n==0:
            print("Cannot remove head pointer")
        ## find the location from the start where the node needs to be removed
        remove = head
        
        for element in range(0,i-n):
             remove = remove.next
        further = remove.next
        remove.next = further.next
        return head

cs = Solution()
n=1
print('n = ',n)
head = cs.removeNthFromEnd(heads,n)
current=head
values = [head.val]
while current.next!=None:
    values.append(current.next.val)
    current = current.next
print("Output Linked List Values after removal",values)
   