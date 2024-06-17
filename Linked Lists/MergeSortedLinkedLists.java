class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        //Create a new linked list which will be your sorted combined linked list
        //Create a dummy node at the front so you are not trying to do .next to null
        ListNode answer =  new ListNode(0);

        //Pointer to iterate and add to answer
        ListNode pointer = answer;

        //Runs until we have reached the end of both list1 and list2
        while ((list1 != null) || (list2 != null)){
            //For when we reach the end of list1 before the end of list2
            //Add the rest of list 2 to answer
            if (list1 == null){
                pointer.next = new ListNode (list2.val);
                list2 = list2.next;
            }

            //For when we reach the end of list2 before the end of list1
            //Add the rest of list1 to answer
            else if (list2 == null){
                pointer.next = new ListNode (list1.val);
                list1 = list1.next;
            }

            else {
                //If current value of list1 > list2:
                //Add current value of list2 to answer via pointer
                if (list1.val > list2.val){
                    pointer.next = new ListNode(list2.val);
                    list2 = list2.next;
                }
                //If current value of list1 <= list2:
                //Add current value of list1 to answer via pointer
                else if (list1.val <= list2.val){
                    pointer.next = new ListNode (list1.val);
                    list1 = list1.next;
                }
            }

            //Move pointer
            pointer = pointer.next;
        }
        //Output
        return answer.next;
    }
}
