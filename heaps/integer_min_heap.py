
class MinHeap:
    def __init__(self, heap_size: int = 10):
        '''Initialize an integer-only min heap structure with a given size defaulted to 10.'''
        self.heap_size = heap_size
        self.min_heap = [0] * (heap_size + 1)
        self.current_size = 0  # Number of elements in the heap.

    def __str__(self):
        return str(self.min_heap[1 : self.current_size + 1])
    
    # Helper methods.
    def parent_index(self, idx: int) -> int:
        return idx // 2

    def left_child_index(self, idx: int) -> int:
        return idx * 2

    def right_child_index(self, idx: int) -> int:
        return (idx * 2) + 1

    def keep_gt_right(self, idx_left: int, idx_right: int):
        '''Maintains complete binary properties by keeping larger items on the right hand side.'''
        if self.min_heap[idx_left] > self.min_heap[idx_right]:
            self.min_heap[idx_left], self.min_heap[idx_right] = \
                                     self.min_heap[idx_right], self.min_heap[idx_left]
        else:
            pass

    def size(self) -> int:
        '''Return the number of elements in the heap.'''
        return self.current_size
    
    def is_empty(self) -> bool:
        '''Check if the heap is empty.'''
        return self.current_size == 0

    def insert(self, element: int):
        '''Add an element to the heap.'''
        if self.current_size >= self.heap_size:
            print('Increase heap_size to add another element.')
            return

        self.current_size += 1
        self.min_heap[self.current_size] = element
        self.bubble_up(self.current_size)

    def bubble_up(self, idx: int):
        '''Maintains complete binary properties by moving new element to correct position.'''
        # If the current node is smaller than its parent, swap until we get to the root node.
        while idx > 1:
            self.keep_gt_right(self.parent_index(idx), idx)
            idx = self.parent_index(idx)  # Move up to the parent's position.

    def peek(self) -> int:
        '''Look at the top element of the heap without removal.'''
        if self.current_size == 0:
            return None
        return self.min_heap[1]
    
    def pop(self) -> int:
        '''Remove the top element from the heap.'''
        if self.current_size == 0:
            raise Exception

        minimum = self.min_heap[1]  # Root should always contain minimum value.
        self.min_heap[1] = self.min_heap[self.current_size]  # Move the last element to the root position.
        self.current_size -= 1
        index = 1
        self.bubble_down(index)  # Bubble down the new root to its correct position

        return minimum

    def bubble_down(self, idx):
        '''Maintains complete binary properties by moving root element to correct position.'''
        while idx <= self.parent_index(self.current_size):  # When the deleted element is not a leaf node.
            min_child_idx = self.find_smaller_child_idx(idx)

            # If the current node is larger than its child node, swap.
            self.keep_gt_right(idx, min_child_idx)

            # Keep larger child leaf on the right-hand side.
            self.keep_gt_right(min_child_idx, self.left_child_index(idx))
            idx = min_child_idx  # Move down to the child's position.

    def find_smaller_child_idx(self, idx: int) -> int:
        '''Finds the smallest child node from the parent index.'''
        if self.right_child_index(idx) > self.current_size:  # No right child.
            return self.left_child_index(idx)
        
        if self.min_heap[self.left_child_index(idx)] < self.min_heap[self.right_child_index(idx)]:
            return self.left_child_index(idx)
        else:
            return self.right_child_index(idx)
    
    def heapify(self, list_to_heap: list[int]):
        '''Convert an integer-only list into a min heap structure in-place.'''
        self.current_size = len(list_to_heap)
        self.min_heap = [0] + list_to_heap[:]
        idx = self.current_size // 2  # Start from the middle of the list.
        while idx > 0:
            self.bubble_down(idx)
            idx -= 1

    def resize(self, new_size: int):
        '''Resize the heap to a new size.'''
        if new_size < self.current_size:
            raise ValueError("New size must be larger than current size.")
        # In a real scenario, you might use a fixed-size array. Here, since we're using Python lists which are dynamic, 
        # the resize operation doesn't need to manually expand the list as it'll grow as needed.
        # Still, if you want to preallocate space for some reason, you can append placeholder values.
        for _ in range(new_size - self.current_size):
            self.min_heap.append(None)


if __name__ == "__main__":
    # Test 1: Initializing an empty heap.
    heap = MinHeap()
    print(f"Initialized empty heap: {heap}")

    # Test 2: Inserting elements.
    numbers = [5, 3, 8, 1, 4, 6]
    for num in numbers:
        heap.insert(num)
        # print(f"inserting {num}: {heap}")
    print(f"After inserting {numbers}: {heap}")

    # Test 3: Peeking.
    print(f"Peeked minimum value: {heap.peek()}")

    # Test 4: Extracting minimum value.
    minimum = heap.pop()
    print(f"Extracted minimum value: {minimum}")
    print(f"After extraction: {heap}")

    # Test 5: Checking size and empty status.
    print(f"Heap size: {heap.size()}")
    print(f"Is heap empty? {heap.is_empty()}")

    # Test 6: Extracting until empty.
    while not heap.is_empty():
        print(f"Extracting: {heap.pop()}, {heap}")
    print(f"After extracting all elements: {heap}")
