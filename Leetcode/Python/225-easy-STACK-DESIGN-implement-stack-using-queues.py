# 225. Implement Stack using Queues
# Easy
# Stack, Design, Queue
# https://leetcode.com/problems/implement-stack-using-queues/
#
# Implement a last-in-first-out (LIFO) stack using one or two queues.

from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
