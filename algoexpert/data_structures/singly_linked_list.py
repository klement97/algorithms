from typing import Any, Optional

from algoexpert.data_structures.node import Node


class LinkedList:
    __slots__ = ['head']

    def __init__(self, head: Node = None):
        self.head = head

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.nxt

    def __repr__(self):
        return ''.join([
            f'{node.value}' + (f' -> ' if node.nxt else '')
            for node in self
        ])

    def _get_last_node(self):
        last_node = None
        for node in self:
            last_node = node

        return last_node

    def _get_last_two_nodes(self) -> tuple[Node, Optional[Node]]:
        previous_node, last_node = self.head, None
        node = self.head
        while node.nxt is not None:
            previous_node = node
            last_node = node.nxt
            node = node.nxt

        return previous_node, last_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self._get_last_node()
            last_node.nxt = new_node

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_head = Node(data, nxt=self.head)
            self.head = new_head

    def pop(self) -> Any:
        if self.head is None:
            raise ValueError('Trying to pop on an empty list raises ValueError')

        previous_node, last_node = self._get_last_two_nodes()
        if last_node is None:
            # Only head is present, remove it.
            data = self.head.value
            del self.head
            self.head = None
            return data

        else:
            data = last_node.value
            del last_node
            previous_node.nxt = None
            return data

    def popleft(self) -> Any:
        if self.head is None:
            raise ValueError('Trying to pop on an empty list raises ValueError')

        second_node = self.head.nxt
        data = self.head.value
        del self.head
        self.head = second_node

        return data
