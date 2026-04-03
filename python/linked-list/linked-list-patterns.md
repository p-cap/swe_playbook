# LinkedList patterns (TWO POINTER)

## General Pattern 
- BASE CASE: Check for `head` or `head.next` for NoneType
- Assign the fast and slow pointer by assigning them to head
```
slow = head
fast = head
```
- Iterate through linkedList is `fast` and `fast.next` has the while loop elements
- `slow` takes one step
- `fast` takes two steps
```
while fast and fast.next
    slow = slow.next 
    fast = fast.next.next
```

## LinkedList cycle
- take the General pattern and check for collision inside the while loop
- return True if there is a collision
```
if slow == fast:
    return True
```

## Middle Element
- take the General pattern 
- return `slow`

## LinkedList is palindrome
- after general pattern, take the middle node which is `slow` node
- create a reverse function to reverse the second half of the linkedlist
- NOTE: Reverse LinkedList problem
```python
def _reverse_list(self, node):
    previous = None
    current = node

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous
```
- We save the return from the reverse_list function
- We iterate through head and the reverse list
- If they are not equal, we return `False`
- If the while loop finishes, we return `True`
```
reverse_list = self.reverse_list(slow)
p1 = head
p2 = reverse_list

while p2:
    if p1.val != p2.val:
        return False
    p1 = p1.next
    p2 = p2.next
return True
```

## LinkedList 2
- We use the general pattern
- inside the while loop, we check for fast and slow collision
- once the collision occurs, set the two pointer again
- `pt1 = head` and `pt2 = slow`
- while for pt1 and pt2 collision
- return `pt1`
```python
            if slow == fast:
                # Phase 2: find cycle start
                ptr1 = head
                ptr2 = slow  # meeting point

                
                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next

                return ptr1  # or ptr2, same node
```