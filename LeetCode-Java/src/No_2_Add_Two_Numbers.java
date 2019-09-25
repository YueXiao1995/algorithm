import java.util.Arrays;

public class No_2_Add_Two_Numbers {

	public static void main(String[] args) {
		Solution2 s = new Solution2();
		// list 1
		ListNode root1 = new ListNode(2);
		ListNode node2 = new ListNode(4);
		ListNode node3 = new ListNode(3);
		
		root1.next = node2;
		node2.next = node3;
		
		// list 1
		ListNode root2 = new ListNode(5);
		ListNode node4 = new ListNode(6);
		ListNode node5 = new ListNode(4);
		
		root2.next = node4;
		node4.next = node5;
		
		s.printList(s.addTwoNumbers(root1, root2));
	}

}

class Solution2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
       return l2;
    }
    
    public void printList(ListNode l1) {
    	while (l1 != null) {
    		System.out.print(l1.val);
    		l1 = l1.next;
    	}
    }
}
