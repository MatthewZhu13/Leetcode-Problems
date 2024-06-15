# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        #If head has no nodes or only one node, there is not need to swap anything
        if not head or not head.next:
            return head

        #Sets the a new temporary head where the next swap will begin
        new_head = head.next.next

        #Swaping the frist two nodes
        head, head.next = head.next, head

        #Setting the 3rd node down the line as the next recursive call as that where the next pair will start
        head.next.next = self.swapPairs(new_head)

        #output
        return head
