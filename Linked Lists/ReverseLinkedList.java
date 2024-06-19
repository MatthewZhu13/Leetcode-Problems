class Solution {
    public ListNode reverseList(ListNode head) {

        /*
        Approach:
        1. You want to have three pointers active
        2. One pointer points at the current node whose .next you want to change (curr)
        3. One pointer points at the previous node who you want to redirect curr.next to (prev)
        4. One pointer points at the next node so that you can move curr and prev forward after changing curr.next to prev
        */
        if ((head == null) || (head.next == null)){
            return head;
        }

        ListNode prev = null;
        ListNode curr = null;
        ListNode ahead = head;
        
        while (ahead != null){
            //Points curr to current node whose .next you want to redirect
            curr = ahead;
            //Moves ahead pointer up before that bridge is burned
            ahead = ahead.next;
            //Reasigns where curr.next is pointing from in front of it to behind it
            curr.next = prev;
            //Moves up prev
            prev = curr;
            
        }
        return prev;
    }
}
