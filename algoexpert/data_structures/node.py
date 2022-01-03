from typing import Optional


class Node:
    __slots__ = ['data', 'nxt']

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt: Optional[Node] = nxt

    def __repr__(self):
        return str(self.data)
