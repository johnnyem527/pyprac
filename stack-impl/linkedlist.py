class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_start_from_list(self):
        # []
        if not self.__root:
            raise RuntimeError("List already empty")
        # [__root, None]
        # [__root, x, None]
        remove_node = self.__root
        # this is ref assignment, not a copy
        # that means first node and second node are the same node,
        # they pointing to the same address, which is the address of the second node
        # in other words, the previous first node has been deleted from list
        self.__root = self.__root.get_next()
        return remove_node

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, text):
        marker = self.__root
        while marker:
            if marker.text == text:
                return marker
            marker = marker.get_next()
        raise LookupError("Node with text {} not found in Linked List".format(text))

    def size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count
