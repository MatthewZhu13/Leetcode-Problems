# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        #Recursive basecase that stops when end of linked list is reachhed
        if head == None or head.next == None:
            return head

        #Temp variable that points to second half of pair
        temp = head.next
        #Points the first half of pair to start of next pair and does above process with next pair
        head.next = self.swapPairs(temp.next)
        
        #Points second half of pair to first half of pair
        temp.next = head  

        #Final output
        return temp

