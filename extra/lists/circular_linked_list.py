import operator

# from linked_list import Node, LinkedList
from extra.lists.linked_list import Node, LinkedList




class CircularLinkedList(LinkedList):
    """Basic object for the Circular Linked List"""
    def _create_instance(self):
        return CircularLinkedList()
    

    ##############################      PRINT     ##############################
    def __repr__(self):
        """Represents the Circular linked list as a string
        ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ 
        │ 1 │⟶│ 2 │⟶│ 3 │⟶│ 4 │⟶│ 5 │⟶│ 6 │⟶│ 7 │⟶ ┐
        └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  │
           ↑                                       │
           └───────────────────────────────────────┘
        """
        if super().is_empty():
            return super()._print_empty_linked_list()
        first_line, second_line, third_line = \
                super()._print_linked_list(self._head)
        # backtrace representation
        second_line += [' ┐']
        third_line  += [' │']

        first_line  = "".join(first_line)
        second_line = "".join(second_line)
        third_line  = "".join(third_line)

        head_data = str(self._head.get_data())
        left_offset = (len(head_data)+4)//2
        remaining = (len(second_line) - 2) - left_offset
        
        fourth_line = (' '*left_offset) + '↑' + (' '*(remaining)) + '│'
        fifth_line  = (' '*left_offset) + '└' + ('─'*(remaining)) + '┘'
        return "{}\n{}\n{}\n{}\n{}".format(\
            first_line, second_line, third_line, fourth_line, fifth_line)


    ##############################     SEARCH     ##############################
    def _validate_index(self, idx, accept_negative=False, accept_slice=False):
        if isinstance(idx, slice):
            if not accept_slice:
                raise IndexError(\
                    "Slice indexing isn't supported with this functinoality!!")
        elif type(idx) != int:
            raise TypeError("Indices must be an integer!")
        elif idx <= -1 and not accept_negative:
            raise IndexError(\
                "Negative indexing isn't supported with this functinoality!!")


    def __getitem__(self, idx):
        """Retrieves the element at the given index."""
        self._validate_index(idx)
        if self.is_empty():
            raise IndexError(f"{self.__module__} is empty!!")
        idx = idx % self._length if self._length != 0 else 0
        return super().__getitem__(idx)


    ##############################     INSERT     ##############################
    def _insert_node(self, prev_node, new_node):
        assert isinstance(new_node, self._basic_node)
        assert new_node.get_data() is not None

        # start inserting the node
        if self._length == 0:
            new_node.set_next(new_node)
            self._head = new_node
        elif prev_node is None:
            new_node.set_next(self._head.get_next())
            self._head.set_next(new_node)
            #swap data between new_node and self._head
            new_node._data, self._head._data = self._head._data, new_node._data
            new_node = self._head #to be returned
        else:
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        self._length += 1
        return new_node
    
    
    def insert(self, idx, item):
        self._validate_index((idx))
        self._validate_item(item)
        idx = idx % (self._length+1)
        super()._insert(idx, item)


    ##############################       SET      ##############################
    def __setitem__(self, idx, item):
        self._validate_index(idx)
        idx = idx % self._length if self._length != 0 else 0
        super()._replace_node(idx, item)
    

    ##############################     REMOVE     ##############################
    def _remove_node(self, prev_node, node_to_be_removed):
        assert prev_node is None or isinstance(prev_node, self._basic_node)
        assert isinstance(node_to_be_removed, self._basic_node)

        # if node to be removed is the first
        if prev_node is None:
            if self._length == 1:
                self._head._data = None #NOTE: don't use set_data() here
            else:
                next_to_head = self._head.get_next()
                self._head.set_data(next_to_head.get_data())
                self._head.set_next(next_to_head.get_next())
        else:
            prev_node.set_next(node_to_be_removed.get_next())
        self._length -= 1
    

    def __delitem__(self, idx):
        """Removes a node at index=idx from the Circular Linked List"""
        self._validate_index(idx)
        if not self.is_empty():
            idx = idx % self._length if self._length != 0 else 0
            node = super()._remove_idx(idx)
            return node


    ############################## MISC ##############################
    def split(self, idx):
        self._validate_index(idx)
        idx = idx % self._length if self._length != 0 else 0
        return super()._split(idx)
    

if __name__ == "__main__":

    ll_1 = CircularLinkedList.from_iterable([2])
    print(ll_1)