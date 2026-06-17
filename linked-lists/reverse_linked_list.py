from singly_linked_list import LinkedList, Node

def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)
    print("Original:")
    ll.display()
    ll.head = reverse(ll.head)
    print("Reversed:")
    ll.display()
