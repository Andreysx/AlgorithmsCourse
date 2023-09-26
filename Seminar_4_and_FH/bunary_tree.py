from numbers import Number
from types import NoneType


class Node:
    """
    Basic tree Node class
    Just store values

    Methods:
        __init__: constructor
        __repr__: Obj representation logic for print and str methods
        __lt__ and __gt__: allow to use compare operations '<' and '>'
    """
    def __init__(self, value: object):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

    def __lt__(self, other) -> bool:
        if not isinstance(other, type(self)):
            raise TypeError(f"Unable to compare {type(self).__name__} and {type(other).__name__} objects")
        return self.value.__lt__(other.value)

    def __gt__(self, other) -> bool:
        if not isinstance(other, type(self)):
            raise TypeError(f"Unable to compare {type(self).__name__} and {type(other).__name__} objects")
        return self.value.__gt__(other.value)


class BinaryTree:
    """
    BinaryTree class.
    Implements Binary tree

    Attributes:
        _allowed_types_: tuple[object]
          Manage what objects allowed to be stored inside tree elements
          Objects must implement at least __lt__ and __gt__ methods
        _new_node_: type
          Controls which object will provide tree node element

    Methods:
        __init__(root: _allowed_types_ | NoneType = None)
          Constructor, create empty tree, or set root element as Node, or create root element with $root as value
        add(value: _allowed_types_) -> None
          Add elements to tree. Checks value type against _allowed_types_
        remove(value: _allowed_types_) -> None
          Search element in tree by $value and delete it
        search(value: _allowed_types_) -> Node | None
          Search element in tree and return it or None
        print(node: Node | None = None, filter_none: bool = False) -> None
          Print tree starting from $node or tree.root
          If $filter_none is set, then mask all 'None' values to empty elements
        __len__: allow to use build in len() function over object
    """
    # _allowed_types_ contains Node as an example
    _allowed_types_ = (Node, Number)

    _new_node_ = Node

    def __init__(self, root: object | None = None):
        if isinstance(root, (Node, NoneType)):
            self.root = root
        else:
            self.root = None
            self.add(root)

    def __len__(self):
        """
        reuse _get_as_rows_ method and count non-empty elements
        """
        return len([True for row in self._get_as_rows_(self.root) for el in row if el is not None])

    def add(self, value: _allowed_types_) -> None:
        """
        Add elements to tree. Checks value type against _allowed_types_

        Parameters:
            value: Value to add

        Raises:
            TypeError: on incorrect value type
            ValueError: if Node with value already in tree
        """
        if not isinstance(value, self._allowed_types_):
            allowed_type_names = [t.__name__ for t in self._allowed_types_]
            raise TypeError(f"For value expected one of types {allowed_type_names}, got {type(value).__name__}")
        node, parent = self._search_(value, self.root)
        if node is None:
            el = self._new_node_(value)
            if parent is None:
                self.root = el
            else:
                if value < parent.value:
                    parent.left = el
                else:
                    parent.right = el
        else:
            raise ValueError(f"Element with value {value} already exists in the tree")

    def remove(self, value: _allowed_types_) -> None:
        """
        Search element in tree by $value and delete it

        Parameters:
            value: Value to remove

        Raises:
            ValueError: if Node with value not exist in tree
        """
        node, parent = self._search_(value, self.root)
        if node:
            if node.left is None and node.right is None:
                new_child = None
            elif node.left and node.right:
                right_min_node, right_min_node_parent = self._min_(node.right)
                if right_min_node_parent:
                    right_min_node_parent.left = None
                right_min_node.left = node.left
                if right_min_node != node.right:
                    right_min_node.right = node.right
                new_child = right_min_node
            else:
                new_child = node.left if node.left else node.right
            if node.value < parent.value:
                parent.left = new_child
            else:
                parent.right = new_child
        else:
            raise IndexError(f"Unable to delete value {value} that is not in the tree")

    def _search_(self, value: _allowed_types_,
                 node: Node,
                 parent: Node | None = None) -> tuple[Node | None, Node | None]:
        """
        Internal search method
        Search for Node with $value and its parent
        Search starts on $node

        Parameters:
            value: Value to search
            node: from which Node start search
            parent(optional): points on current node parent, used for recursion purposes
        """
        if node is None or node.value == value:
            return node, parent
        if value < node.value:
            return self._search_(value, node.left, node)
        else:
            return self._search_(value, node.right, node)

    def search(self, value: _allowed_types_) -> Node | None:
        """
        Search element in tree and return it or None
        Search always starts on tree root

        Parameters:
            value: Value to search
        """
        return self._search_(value, self.root)[0]

    @staticmethod
    def _get_as_rows_(node: Node) -> list[list[_allowed_types_]]:
        """
        Represent tree as rows
        Including None elements

        Parameters:
            node: from which Node start
        """
        result = list()
        if node is not None:
            next_row = [node.left, node.right]
            result.append([node])
            while len([el for el in next_row if el is not None]) > 0:
                curr_row = next_row
                next_row = list()
                row_data = list()
                for el in curr_row:
                    row_data.append(el)
                    if el:
                        next_row.append(el.left)
                        next_row.append(el.right)
                    else:
                        next_row.append(None)
                        next_row.append(None)
                result.append(row_data)
        return result

    @staticmethod
    def _max_(node: Node) -> tuple[Node | None, Node | None]:
        """
        Search max element in tree starting on $node

         Parameters:
            node: from which Node start
        """
        parent = None
        if node:
            while node.right:
                parent = node
                node = node.right
        return node, parent

    @staticmethod
    def _min_(node: Node) -> tuple[Node | None, Node | None]:
        """
        Search min element in tree starting on $node

        Parameters:
            node: from which Node start
        """
        parent = None
        if node:
            while node.left:
                parent = node
                node = node.left
        return node, parent

    def print(self, node: Node | None = None, filter_none: bool = False) -> None:
        """
        Print tree starting from $node or tree root
        If $filter_none is set, then mask all 'None' values to empty elements

         Parameters:
            node(optional): from which Node start search, use tree root if not set
            filter_none(optional): mask all 'None' values to empty elements when set
        """

        if not node:
            node = self.root
        tree_rows = self._get_as_rows_(node)
        if filter_none:
            tree_rows = [[el if el is not None else ' ' for el in row] for row in tree_rows]
        longest_row_len = max((len(row) for row in tree_rows), default=0)
        # max tree element does not have to be the longest
        # so search for longest by checking len(str(el))
        longest_el_size = max((len(str(el)) for row in tree_rows for el in row), default=0)+1
        for row in tree_rows:
            print(''.join(str(el).center(longest_el_size*longest_row_len//len(row)) for el in row))


if __name__ == '__main__':
    print("This is internal class, launch main.py")