class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = value

    def get_head_node(self):
        return self.head_node

    def insert_new_node(self, new_value):                   # Takes new node, adds to the beginning of the list
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)              # new_node -> old_node
        self.head_node = new_node                           # becomes the beginning of the list

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node                                # Starts at the beginning of the list
        while current_node:                                          # Creates loop
            if current_node.get_value():                             # checks if last node, if is breaks loop
                string_list += str(current_node.get_value()) + "/n"
            current_node = current_node.get_next_node()              # Progresses to next node if loop continues
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node == value_to_remove:
            self.head_node = current_node.get_next_node()                   # checks if first node, before looping
        else:
            while current_node:                                             # creates loop
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove():              # Orphans the next node: # n1 -> n2 - > n3
                    current_node.set_next_node(next_node.get_next_node())   # {n1} -> {n2} - > {n3} becomes {n1} -> {n3}
                else:
                    current_node = next_node                                # continues loop

    def remove_all_instances(self, value_to_remove):

