from algoexpert.data_structures.singly_linked_list import LinkedList


def remove_duplicates(linked_list: LinkedList):
    """
    Remove duplicates from an already sorted linked list.
    """
    node = linked_list.head
    while node:
        next_distinct_node = node.nxt
        while next_distinct_node and next_distinct_node.value == node.value:
            next_distinct_node = next_distinct_node.nxt

        node.nxt = next_distinct_node
        node = next_distinct_node
