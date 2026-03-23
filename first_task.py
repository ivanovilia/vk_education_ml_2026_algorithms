
class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

def intersection(listA, listB):
    pointerA, pointerB = listA, listB

    while pointerA != pointerB:
        
        if pointerA:
            pointerA = pointerA.next
        else:
            pointerA = listB

        if pointerB:
            pointerB = pointerB.next
        else:
            pointerB = listA    
            
    return pointerA    


commonPart = ListNode(1)
commonPart.next = ListNode(8)
commonPart.next.next = ListNode(4)
commonPart.next.next.next = ListNode(5)

A = ListNode(4)
A.next = commonPart

B = ListNode(5)
B.next = ListNode(6)
B.next.next = commonPart

result = intersection(A, B)
assert result == commonPart

print("Успех")


