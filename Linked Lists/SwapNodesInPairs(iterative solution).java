class Solution {
    public ListNode findKth(ListNode top){
        //Find the second node of each pair
        for (int i = 0; i < 2; i++){
            if (top == null){
                break;
            }
            top = top.next;
        }
        return top;
    }


    public ListNode swapPairs(ListNode head) {
        //Create a dummy node
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        //Keep a pointer at the front of the linked list to return as the answer
        ListNode ans = dummy;

        //Return head if there is no elements or only 1 element in the linked list
        if ((head == null) || (head.next == null)){
            return head;
        }

        ListNode kth = findKth(dummy);
        ListNode prev;
        ListNode curr;
        ListNode temp;

        while (kth != null){
            //Point prev to first node in each pair
            prev = dummy.next;
            //Point curr to the second node in each pair
            curr = kth;

            //Store the start of the next pair of nodes as once you redirect curr.next, you break the link between the two
            temp = kth.next;
            //Point the second node in the pair to the first node
            curr.next = prev;

            //Point the first node in the pair (now last) to the first node in the next pair (temp)
            prev.next = temp;

            //Repoint dummy.next to the first node of the pair
            dummy.next = curr;

            //Move kth back to the 2nd node of the pair
            kth = kth.next;

            //Move kth to the next pair
            kth = findKth(kth);
            if (kth != null){
                //Move dummy node to the node before the next pair
                dummy = dummy.next.next;
            }
        }

        return ans.next;


    }
}
