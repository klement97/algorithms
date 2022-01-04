from typing import Any, Optional

from algoexpert.data_structures.node import DNode


class DoubleLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head if head is None else DNode(head)
        self.tail = tail if tail is None else DNode(tail)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.nxt

    def __repr__(self):
        return ''.join([
            f'{node.value}' + (f' -> ' if node.nxt else '')
            for node in self
        ])

    def append(self, value):
        node = DNode(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.nxt = node
            self.tail = node

    def prepend(self, value):
        node = DNode(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head.prev = node
            self.head = node

    def _pop(self) -> Optional[Any]:
        if self.head is None:
            raise ValueError('Trying to pop on an empty list raises ValueError')

        if self.head is self.tail:
            value = self.head.value
            del self.head
            del self.tail
            self.head = None
            self.tail = None

            return value

    def pop(self) -> Any:
        value = self._pop()
        if value:
            return value

        value = self.tail.value
        prev = self.tail.prev
        prev.nxt = None
        del self.tail
        self.tail = prev

        return value

    def popleft(self):
        value = self._pop()
        if value:
            return value

        value = self.head.value
        second_node = self.head.nxt
        second_node.prev = None
        del self.head
        self.head = second_node

        return value
