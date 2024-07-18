class Solution(object):
    def modifiedList(self, nums, head):
        if not head:
            return head
 
        #Turn nums into a hashset so .contains() will have O(1) time
        my_set = set(nums)

        #Create a sentinel node, a prev node pointing to sentinel, and a curr node pointing to head
        sentinel = ListNode(0, head)
        prev = sentinel
        curr = head

        while curr:
            #Check if curr is in the hashset
            if curr.val in my_set:
                #skip over the current node if it is in my_set
                prev.next = curr.next
                #move curr forward but not prev as you do not know if the new curr node is in my_set or not
                curr = curr.next
            
            #If current node is not in hashet, increment both prev and curr
            else:
                prev = curr
                curr = curr.next

        return sentinel.next
