from arrDoublyLinkedList import arrayDoublyLinkedList
from doublyLinkedList import DoublyLinkedList


def demo_arr_doubly_linked_list():
    print("Demonstrating arrayDoublyLinkedList")

    print("\n1. Creating a list")
    adll = arrayDoublyLinkedList()
    print(f"Created an empty list. Length: {adll.length()}")

    print("\n2. Adding elements (append)")
    adll.append('a')
    adll.append('b')
    adll.append('c')
    print(f"Added elements 'a', 'b', 'c'. Length: {adll.length()}")
    print("List contents:", [adll.get(i) for i in range(adll.length())])

    print("\n3. Inserting elements (insert)")
    adll.insert('x', 1)
    adll.insert('y', 0)
    adll.insert('z', adll.length())
    print(f"Inserted 'x' at position 1, 'y' at 0, 'z' at the end. Length: {adll.length()}")
    print("List contents:", [adll.get(i) for i in range(adll.length())])

    print("\n4. Removing an element by index (delete)")
    removed = adll.delete(2)
    print(f"Removed element at position 2: '{removed}'")
    print("List contents:", [adll.get(i) for i in range(adll.length())])

    print("\n5. Removing all occurrences of an element (deleteAll)")
    adll.append('a')
    adll.append('a')
    print("Added two 'a' elements")
    print("List contents before removal:", [adll.get(i) for i in range(adll.length())])
    adll.deleteAll('a')
    print("Removed all 'a' elements")
    print("List contents:", [adll.get(i) for i in range(adll.length())])

    print("\n6. Finding the first occurrence (findFirst)")
    adll.append('b')
    adll.append('c')
    print("Added 'b' and 'c'")
    index = adll.findFirst('b')
    print(f"First occurrence of 'b' at position: {index}")
    index = adll.findFirst('nonexistent')
    print(f"Search for nonexistent element: {index}")

    print("\n7. Finding the last occurrence (findLast)")
    adll.append('b')
    print("Added another 'b'")
    index = adll.findLast('b')
    print(f"Last occurrence of 'b' at position: {index}")

    print("\n8. Cloning the list (clone)")
    clone = adll.clone()
    print(f"Cloned the list. Clone length: {clone.length()}")
    print("Clone contents:", [clone.get(i) for i in range(clone.length())])
    clone.append('new')
    print("Added 'new' to the clone")
    print("Original:", [adll.get(i) for i in range(adll.length())])
    print("Clone:", [clone.get(i) for i in range(clone.length())])

    print("\n9. Reversing the list (reverse)")
    print("List before reversing:", [adll.get(i) for i in range(adll.length())])
    adll.reverse()
    print("List after reversing:", [adll.get(i) for i in range(adll.length())])

    print("\n10. Extending the list (extend)")
    other = arrayDoublyLinkedList()
    other.append('1')
    other.append('2')
    print("Other list:", [other.get(i) for i in range(other.length())])
    adll.extend(other)
    print("Current list after extending:", [adll.get(i) for i in range(adll.length())])

    print("\n11. Clearing the list (clear)")
    adll.clear()
    print(f"List cleared. Length: {adll.length()}")

    print("\n12. Error handling")
    try:
        adll.insert('x', 1)
    except IndexError as e:
        print(f"Insert error: {e}")

    try:
        adll.get(0)
    except IndexError as e:
        print(f"Get error: {e}")


def print_list(dll):
    elements = []
    current = dll.head
    while current:
        elements.append(current.value)
        current = current.next
    print(f"List: {elements}, Length: {dll.length()}")

def demo_doubly_linked_list():
    print("\nDemonstrating DoublyLinkedList")

    print("\n1. Creating a list")
    dll = DoublyLinkedList()
    print(f"Created an empty list. Length: {dll.length()}")

    print("\n2. Adding elements (append)")
    dll.append('A')
    dll.append('B')
    dll.append('C')
    print_list(dll)

    print("\n3. Inserting elements (insert)")
    dll.insert('X', 1)
    dll.insert('Y', 0)
    dll.insert('Z', dll.length())
    print("Inserted 'X' at position 1, 'Y' at 0, 'Z' at the end")
    print_list(dll)

    print("\n4. Removing an element by index (delete)")
    removed = dll.delete(2)
    print(f"Removed element at position 2: '{removed}'")
    print_list(dll)

    print("\n5. Removing all occurrences of an element (deleteAll)")
    dll.append('B')
    dll.append('B')
    print("Added two 'B' elements")
    print_list(dll)
    dll.deleteAll('B')
    print("Removed all 'B' elements")
    print_list(dll)

    print("\n6. Finding the first occurrence (findFirst)")
    dll.append('C')
    dll.append('D')
    print("Added 'C' and 'D'")
    print_list(dll)
    index = dll.findFirst('C')
    print(f"First occurrence of 'C' at position: {index}")
    index = dll.findFirst('Nonexistent')
    print(f"Search for nonexistent element: {index}")

    print("\n7. Finding the last occurrence (findLast)")
    dll.append('C')
    print("Added another 'C'")
    print_list(dll)
    index = dll.findLast('C')
    print(f"Last occurrence of 'C' at position: {index}")

    print("\n8. Cloning the list (clone)")
    clone = dll.clone()
    print("Cloned the list:")
    print("Original:", end=" ")
    print_list(dll)
    print("Clone:", end=" ")
    print_list(clone)
    clone.append('New')
    print("Added 'New' to the clone")
    print("Original:", end=" ")
    print_list(dll)
    print("Clone:", end=" ")
    print_list(clone)

    print("\n9. Reversing the list (reverse)")
    print("Before reversing:", end=" ")
    print_list(dll)
    dll.reverse()
    print("After reversing:", end=" ")
    print_list(dll)

    print("\n10. Extending the list (extend)")
    other = DoublyLinkedList()
    other.append('1')
    other.append('2')
    print("Other list:", end=" ")
    print_list(other)
    dll.extend(other)
    print("Current list after extending:", end=" ")
    print_list(dll)

    print("\n11. Clearing the list (clear)")
    dll.clear()
    print(f"List cleared. Length: {dll.length()}")

    print("\n12. Checking node links")
    dll.append('A')
    dll.append('B')
    dll.append('C')
    print("Added A, B, C")
    print(f"Head: {dll.head.value}, Tail: {dll.tail.value}")
    print(f"Head.next: {dll.head.next.value}, Tail.prev: {dll.tail.prev.value}")

    print("\n13. Error handling")
    try:
        dll.insert('X', 5)
    except IndexError as e:
        print(f"Insert error: {e}")

    try:
        dll.get(10)
    except IndexError as e:
        print(f"Get error: {e}")


if __name__ == "__main__":
    demo_arr_doubly_linked_list()
    demo_doubly_linked_list()
