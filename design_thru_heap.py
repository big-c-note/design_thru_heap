"""
           _________ _________ _________ _________ _________ _________
         |         |         |         |         |         |         |
         |    D    |    E    |    S    |    I    |    G    |    N    |
         |_________|_________|_________|_________|_________|_________|
         |         |
         |    A    |
         |_________|_________ _________ _________
         |         |         |         |         |
         |    H    |    E    |    A    |    P    |
         |_________|_________|_________|_________|

A meditation on design through the heap data structure. As written by Colin and
gpt [1].

Recently, I was practicing leetcode problems, and the assignment I was
given was to implement a heap data structure.

I had been reading A Philosophy of Software Design by John Ousterhout (Great
book), so I found myself asking design questions.

Like, "What is the purpose of a heap?" and "What is the purpose of a heap [2]

[1] (isn't it so interesting the casing doesn't matter?)
[2] GPT wrote this line.
[3] Code by yours truly.
"""
import unittest

# Just some types. Over engineering here I come.
NodeIndex = int
Node = int


class MinHeap:
    """
    Heap there it is. https://en.wikipedia.org/wiki/Heap_(data_structure)


    Parameters
    ----------
    array : list
        A list of integers to be used as the heap.

    Methods
    -------
    peek() -> int
        Returns the minimum value in the heap and removes it from the heap.

    insert(node: int) -> None
        Inserts a node into the heap.
    """

    def __init__(self, array):
        self.heap = array
        self._build_heap()

    def _build_heap(self):
        """
        Construct a heap from an array. `_build_heap` modifies `self.heap` instance
        variable in place.

        Returns
        -------
        None
        """

        # Iterate through the heap from the last parent through the first
        # parent and sift down until the heap invariant is satisfied.

        last_parent_i = (len(self.heap) - 2) // 2
        for parent_i in range(last_parent_i, -1, -1):
            # We modify the underlying heap in place.
            self._sift_down(parent_i=parent_i)

        return

    def peek(self) -> int:
        """
        Returns the minimum value in the heap and removes it from the heap.
        Modifies the `self.heap` instance variable in place.

        Returns
        -------
        min_heap_value : int
        """

        # Swap first and last node.
        first_node_i = 0
        last_node_i = len(self.heap) - 1
        self.heap[first_node_i], self.heap[last_node_i] = (
            self.heap[last_node_i],
            self.heap[first_node_i],
        )

        min_heap_value = self.heap.pop()
        # We modify the heap in place.
        self._sift_down(parent_i=0)

        return min_heap_value

    def insert(self, node: int) -> None:
        """
        Inserts a node into the heap, maintaining the heap invariant.

        Returns
        -------
        None
        """
        self.heap.append(node)
        node_i = len(self.heap) - 1
        self._sift_up(child_i=node_i)
        return

    def _sift_down(self, parent_i: int = 0) -> None:
        """
        Sift down a node until the heap invariant is satisfied. Modifies the
        heap in place.

        Returns
        -------
        None
        """
        children: dict[Node, NodeIndex] = self._get_children(parent_i=parent_i)
        while children:
            # Get the child with the minimum value and its index.
            parent = self.heap[parent_i]
            min_child = min(children.keys())

            if parent <= min_child:
                break

            min_child_i = children[min_child]
            self.heap[parent_i], self.heap[min_child_i] = (
                self.heap[min_child_i],
                self.heap[parent_i],
            )

            parent_i = min_child_i
            children = self._get_children(parent_i=parent_i)
        return

    def _sift_up(self, child_i: int) -> None:
        """
        Sift up a node until the heap invariant is satisfied.

        Returns
        None
            Modifies the heap in place.
        """
        child = self.heap[child_i]
        parent, parent_i = self._get_parent(child_i=child_i)

        # Swap parent for child until the heap invariant is satisfied.
        while child < parent and child_i > 0:
            self.heap[parent_i], self.heap[child_i] = (
                self.heap[child_i],
                self.heap[parent_i],
            )

            child, child_i = self.heap[parent_i], parent_i
            parent, parent_i = self._get_parent(child_i=child_i)
        return

    def _get_children(self, parent_i: int) -> dict[Node, NodeIndex]:
        """
        Given a parent index, return the children and their indices in a
        dictionary.

        Returns
        -------
        children : dict[Node, NodeIndex]
        """
        left_child_i = parent_i * 2 + 1
        right_child_i = parent_i * 2 + 2

        # If the children exist, grab them.
        children = {}
        if left_child_i < len(self.heap):
            child = self.heap[left_child_i]
            children[child] = left_child_i

        if right_child_i < len(self.heap):
            child = self.heap[right_child_i]
            children[child] = right_child_i

        return children

    def _get_parent(self, child_i: int) -> tuple[Node, NodeIndex]:
        """
        Given a child index, return the parent and its index.
        """
        parent_i: NodeIndex = (child_i - 1) // 2
        parent: Node = self.heap[parent_i]

        return parent, parent_i


class TestMinHeap(unittest.TestCase):
    """
    Tests provided by gPt (sort of).
     ,-.-.
     `. ,'
       `
    """

    def test_build_heap(self):
        heap = MinHeap([3, 2, 1, 4, 5])
        self.assertEqual(heap.heap, [1, 2, 3, 4, 5])

    def test_peek(self):
        heap = MinHeap([3, 2, 1, 4, 5])
        self.assertEqual(heap.peek(), 1)
        self.assertEqual(heap.heap, [2, 4, 3, 5])

    def test_insert(self):
        heap = MinHeap([3, 2, 1, 4, 5])
        heap.insert(0)
        self.assertEqual(heap.heap, [0, 2, 1, 4, 5, 3])

    def test_get_children(self):
        heap = MinHeap([3, 2, 1, 4, 5])
        children = heap._get_children(parent_i=0)
        self.assertEqual(children, {2: 1, 3: 2})

    def test_get_parent(self):
        heap = MinHeap([3, 2, 1, 4, 5])
        parent, parent_i = heap._get_parent(child_i=2)
        self.assertEqual((parent, parent_i), (1, 0))

    def test_is_conscious(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
