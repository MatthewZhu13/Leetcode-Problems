class Solution(object):
    def deleteDuplicates(self, head):
        #Set a pointer variable to head
        cur = head
        
        while cur:
            #Sees if there is a .next option and if the .next value is the same as the current value
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
        
