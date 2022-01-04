class NodePointer:
    """
    Descriptor class for NodePointer (next or previous).
    Validates the following before setting a value:
    - If the value is not None, it must be an instance of Node.
    - If the Node and the NodePointer are the same.
    """

    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, instance, owner=None):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError(f'next value can not be of type different than'
                            f' Node. Value given: {value}')

        if instance is value:
            raise ValueError(f'You can not set next to self.'
                             f'This will cause infinite loop.')

        setattr(instance, self.private_name, value)

    def __delete__(self, instance):
        delattr(instance, self.private_name)


class Node:
    nxt = NodePointer()

    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        return str(self.value)


class DNode(Node):
    prev = NodePointer()

    def __init__(self, value, nxt=None, prev=None):
        super(DNode, self).__init__(value, nxt)
        self.prev: DNode = prev
