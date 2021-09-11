#Tempo: O(max(n,m))
#Espaço: O(max(n,m))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        initial_node = ListNode()
        current_node = initial_node
        while (l1 != None) or (l2!= None):
            current_node.next = ListNode()
            current_node = current_node.next
            current_sum = carry
            if l1 != None:
                current_sum += l1.val
                l1 = l1.next
            if l2 != None:
                current_sum += l2.val
                l2 = l2.next

            carry = int(current_sum/10)
            current_node.val = current_sum % 10
        if carry != 0:
            current_node.next = ListNode()
            current_node.next.val = carry
        
        return initial_node.next