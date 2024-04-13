# 232. Implement Queue using Stacks
# Easy
# Stack, Design, Queue
# https://leetcode.com/problems/implement-queue-using-stacks
#
# Implement a FIFO queue using two stacks.
# The queue should support normal functions: push, peek,pop, and empty.


class MyQueue:
    # Two Stacks | Time: O(1) | Space: O(n)
    def __init__(self):
        self.buffer = []
        self.stack_queue = []

    def push(self, x: int) -> None:
        '''Push element x to the back of queue.'''
        self.buffer.append(x)

    def pop(self) -> int:
        '''Remove the element from the front of the queue and return it.'''
        if self.stack_queue:
            return self.stack_queue.pop()  # Stored in top.
        else:
            self.transfer()
        return self.stack_queue.pop()

    def peek(self) -> int:
        '''Get the front element.'''
        if self.stack_queue:
            return self.stack_queue[-1]  # Look at top.
        else:
            self.transfer()
        return self.stack_queue[-1]

    def empty(self) -> bool:
        '''Determine if the stack is empty.'''
        return not self.stack_queue and not self.buffer

    def transfer(self) -> None:
        if self.stack_queue:
            return  # Some action should have taken place before calling transfer.
        if not self.buffer:
            raise Exception("Queue is empty.")
        while self.buffer:  # Transfer the buffer stack to the queue.
            self.stack_queue.append(self.buffer.pop())


# class MyQueue:
#     # Single list | Time: O(n) Space: O(n)
#     def __init__(self):
#         self.stack = []

#     def push(self, x: int) -> None:
#         '''Push element x to the back of queue.'''
#         for idx, elem in enumerate(self.stack):
#             if elem == x:
#                 del self.stack[idx]
#         self.stack.append(x)

#     def pop(self) -> int:
#         '''Remove the element from the front of the queue and return it.'''
#         popped = self.peek()
#         del self.stack[0]
#         return popped

#     def peek(self) -> int:
#         '''Get the front element.'''
#         return self.stack[0]

#     def empty(self) -> bool:
#         '''Determine if the stack is empty.'''
#         return not self.stack

# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()
