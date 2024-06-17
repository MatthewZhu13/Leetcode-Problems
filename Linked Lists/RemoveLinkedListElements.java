class Solution {
    public ListNode removeElements(ListNode head, int val) {
        //Create a dummy node so that when you can avoid NullPoint Exception when you try to do .next on an empty LinkedList
        ListNode ans = new ListNode(0);
        //Link dummy node and head
        ans.next = head;
        //Create a pointer ListNode to use to iterate through and edit the Linked list
        ListNode pointer = ans;

        while (pointer.next != null){
            //If the next value == val, then you must skip over that node
            if (pointer.next.val == val){
                //If the next next node is null then simply set the next node to null
                if (pointer.next.next == null){
                    pointer.next = null;
                }
                else{
                    //Skipping over val node
                    pointer.next = pointer.next.next;
                }
            }
            //Otherwise move on
            else{
                pointer = pointer.next;
            
            }

        }
        //Output
        return ans.next;
    }
}
