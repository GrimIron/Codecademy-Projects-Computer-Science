class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail

    # More detailed comments then usual as learning the concepts of nodes, and needed more detailed comments to be
    # able to visualise it, will remove in future when comfier with the concept
    def remove_head(self):
        removed_head = self.head_node               # Sets the current head node as one to remove

        if removed_head == None:                    # Checks if there is a head node
            return None

        self.head_node = removed_head.get_next_node()   # Sets the head node to the next node along from former head

        if self.head_node != None:                  # Checks if there is any nodes
            self.head_node.set_prev_node(None)      # Removes pointer from head node to make it the head node

        if removed_head == self.tail_node:          # Checks if the removed head node is also the tail node
            self.remove_tail()                      # If so removes that too

        return removed_head.value

    def remove_tail(self):
        removed_tail = self.tail_node               # Sets the current tail node as one to remove

        if removed_tail == None:                    # Checks if there is a tail node
            return None

        self.tail_node = removed_tail.prev_node     # Sets the tail node to the next node back from former tail

        if self.tail_node != None:                  # Checks if there is any nodes
            self.tail_node.next_node = None         # Removes pointer from tail node to make it the tail node

        if removed_tail == self.head_node:          # Checks if the removed tail node is also the head node
            self.remove_head()                      # If so removes that too

        return removed_tail.value

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()

        # checks if there is a node to remove, if there is it checks if its a tail or head node, and run remove_head()
        # or remove_tail().
        # If it isn't we know the value is in the center of the list, and will change the pointers either side of the
        # node to remove(orphan) it.
        if node_to_remove == None:
            return None
        elif node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.prev_node = prev_node
            prev_node.next_node = next_node
        return node_to_remove












