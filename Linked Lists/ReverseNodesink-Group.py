class Solution(object):
    def getKth(self, current, kNum):
        while current and kNum > 0:
            current = current.next
            kNum -= 1

        if kNum != 0:
            return None
        
        return current

    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy
        # groupPrev -> 1 -> 2 -> 3 -> 4
        # groupPrev -> 2 -> 1 -> 3 -> 4

        while True:
            #Gets us the next kth node
            kth = self.getKth(groupPrev, k)
            #Breaks us out of our while loop when we get to the end of the linked list
            if kth == None: break

            #Reverse the next k nodes
            #Points first node of the group (last after done reversing) to the first node of the next group
            prev = kth.next
            curr = groupPrev.next

            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            
            #Assign temp = groupPrev.next which was originally pointing at the first node of the group  but now is the last
            #k = 2
            # 2 -> 1 -> 3 -> 4    
            # kth  ^   temp
            #      |
            #   groupPrev
            temp = groupPrev.next
            
            #kth originally was the last node of the group but now is the first
            #groupPrev.next repoints the node before the group to the new first node of the group
            groupPrev.next = kth
            #moves groupPrev up from the front of the previous group to the front of the next group
            groupPrev = temp
        
        return dummy.next


        
            
            



            
        
