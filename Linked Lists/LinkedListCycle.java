public class Solution {
    public boolean hasCycle(ListNode head) {
        //Check for special edgecases
        if ((head == null) || (head.next == null)) {
            return false;
        }

        /*
        Approach:
        1. Have 2 pointers (tortise + hare)
        2. Tortise moves forward once every iteration while Hare moves twice
        3. If Hare reaches the end of the linked list, there is no cycle
        4. If Hare eventually equals Tortise, then there is a cycle
        5. If the Linked List is a cycle then the Hare will eventually land on the same node as the Tortise since it covers twice as many nodes as it each iteration
        */
      
        ListNode tortise = head;
        ListNode hare = head;

        //Checks to see if Hare has reached the end of the list
        while ((hare.next != null) && (hare.next.next != null)){
            //Moves tortise forward once
            tortise = tortise.next;
            //Moves hare forward twice
            hare = hare.next.next;

            //Checks to see if the two are on the same node
            if (tortise == hare){
                return true;
            }
        }

        return false;

    }
}
