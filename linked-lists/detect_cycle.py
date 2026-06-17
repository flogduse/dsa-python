from singly_linked_list import LinkedList, Node

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)
    print("Has cycle:", has_cycle(ll.head))
    ll.head.next.next.next.next.next = ll.head.next
    print("Has cycle (after adding):", has_cycle(ll.head))
