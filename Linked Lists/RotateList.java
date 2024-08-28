class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        //since a linked list rotated 1 more than its length is equal to being rotated only once

        if(head == null){return head;}

        //create dummy pointer so that you can swap the first value  
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        //find out how long the linked list is
        int i;
        ListNode counter = dummy;
        for(i = 0; counter.next != null; i++){counter = counter.next;}

        
        ListNode p1 = dummy.next;
        //store the value of the node you are currently on
        int last_val = p1.val;
        //only perform the rotation only rotations % length of linked list times as rotating the linked list length of linked list times results in the same linked list
        for(int j = 0; j < k % i; j++){
            while (p1.next != null){
                //store the value of the node you are rotating the current node to
                int curr_val = p1.next.val;
                //replace the next nodes value with the current nodes value
                p1.next.val = last_val;
                //move the pointer forward
                p1 = p1.next;
                //replace the previous value variable with the value of the node you rotated to  
                last_val = curr_val;
            }
            //at the end of the cylce replace the value of the first node in the linked list with the value of the last node in the linked lsit
            dummy.next.val = last_val;
            //move pointer back to start of the list
            p1 = dummy.next;
        }
        return dummy.next;

    }
}
