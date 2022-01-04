import pytest

from algoexpert.data_structures.node import Node

multiple_values = pytest.mark.parametrize(
    'value',
    [1, 'a', [1], {'a': 1}, {1, 2}]
)


def test_node_without_data_raises_error():
    with pytest.raises(TypeError):
        Node()


@multiple_values
def test_node_can_be_created_with_data(value):
    node = Node(value)
    assert node.value == value


def test_node_data_can_be_none():
    none_node = Node(None)
    assert none_node.value is None


def test_next_is_none_if_not_given():
    node = Node(1)
    assert node.nxt is None


@multiple_values
def test_next_value_other_than_node_raises_error(value):
    with pytest.raises(TypeError):
        Node(1, nxt=value)


@multiple_values
def test_next_value_can_only_be_set_to_node_type(value):
    with pytest.raises(TypeError):
        node = Node(1)
        node.nxt = value


def test_next_can_be_set_to_node():
    node = Node(1)
    node.nxt = Node(2)
    assert node.nxt.value == 2


def test_next_can_be_set_to_none():
    node = Node(1)
    node.nxt = None
    assert node.nxt is None


def test_node_can_be_created_with_data_and_next():
    node = Node(1, nxt=Node(2))
    assert node.value == 1
    assert node.nxt.value == 2


def test_node_can_be_created_with_data_and_next_none():
    node = Node(1, nxt=None)
    assert node.value == 1
    assert node.nxt is None


def test_node_next_referencing_itself_raises_error():
    node = Node(1)
    with pytest.raises(ValueError):
        node.nxt = node
