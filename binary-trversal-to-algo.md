# Binary Tree Traversal Methods

Tree traversals are the different ways to visit every node in a binary tree exactly once. They are broadly categorized into **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** based on the underlying algorithm and data structure used.

### Traversal Comparison Table

| Traversal Category | Traversal Name | Order of Operations | Logic / Core Algorithm | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **DFS** | **Pre-Order** | **Root** $\rightarrow$ Left $\rightarrow$ Right | Process node, then go deep. Uses a **Stack** (or Recursion). | Copying a tree, Prefix expressions. |
| **DFS** | **In-Order** | Left $\rightarrow$ **Root** $\rightarrow$ Right | Go left, process node, go right. Uses a **Stack**. | Sorting a Binary Search Tree (BST). |
| **DFS** | **Post-Order** | Left $\rightarrow$ Right $\rightarrow$ **Root** | Process children, then process node. Uses a **Stack**. | Deleting a tree, Postfix expressions. |
| **BFS** | **Level-Order** | Level by Level (Left to Right) | "Sweep" across each row. Uses a **Queue**. | Shortest path, Tree width, Level-by-level grouping. |

---

### 1. Depth-First Search (DFS) Patterns
DFS algorithms go as deep as possible down one branch before backtracking. Because they follow a "Last-In, First-Out" logic, they are perfectly suited for **Recursion**.



#### Python Templates
Notice how only the position of the `print` (or result append) changes:

```python
# PRE-ORDER
def preOrder(root):
    if root:
        print(root.val)    # ROOT first
        preOrder(root.left)
        preOrder(root.right)

# IN-ORDER
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)    # ROOT middle
        inOrder(root.right)

# POST-ORDER
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)    # ROOT last
```

---

### 2. Breadth-First Search (BFS) Patterns
BFS (Level-Order) ignores the vertical "depth" and focuses on the horizontal "breadth." It uses a **Queue** (First-In, First-Out) to ensure nodes are processed in the order they were discovered.



#### Python Template
```python
from collections import deque

def levelOrder(root):
    if not root: return []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```

---

### Summary Checklist

* **Need it sorted?** Use **In-Order** (on a BST).
* **Need to copy?** Use **Pre-Order**.
* **Need to delete?** Use **Post-Order**.
* **Need the shortest path?** Use **Level-Order**.

