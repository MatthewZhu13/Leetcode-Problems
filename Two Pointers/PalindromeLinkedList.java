class Solution {
    public boolean isPalindrome(ListNode head) {
        if ((head == null) || (head.next == null)){return true;}

        //Iterate through linked list to count if even or odd # of nodes
        int iterator = 0;
        ListNode counter = head;
        while (counter != null){
            iterator += 1;
            counter = counter.next;
        }

        //Put into place fast and slow pointers
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }

        //Reverse first half of linked list
        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode groupPrev = head;
        ListNode curr = head;
        ListNode temp;
        while (curr != slow){
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            
        }

        //If # of nodes is odd then slide slow pointer one to the right
        //Middle value never matters for palindromes
        groupPrev.next = slow;
        if (iterator % 2 == 1){
            slow = slow.next;
        }

        //Compare first half and second half of linked list
        while (slow != null){
            if (prev.val != slow.val){return false;}
            prev = prev.next;
            slow = slow.next;
        }
        

        return true;     
    }
}
