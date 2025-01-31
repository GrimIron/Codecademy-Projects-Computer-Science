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
        self.head_node = None

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
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()              # Progresses to next node if loop continues
        return string_list

    def remove_node(self, node_to_remove):
        current_node = self.head_node                               # checks the head node to see if value to remove

        if current_node.get_value() == node_to_remove:
            self.head_node = current_node.get_next_node()
        else:                                                       # if NOT headnode Starts a loop through the list
            while current_node != None:
                next_node = current_node.get_next_node()            # checks one node ahead
                if next_node == None:
                    return None
                if next_node.get_value() == node_to_remove:                 # if next node is value to remove,
                    current_node.set_next_node(next_node.get_next_node())   # set current_node pointer to skip next node

                current_node = current_node.get_next_node()         # sets the current node to the next node

    def remove_all_instances(self, value_to_remove):
        current_node = self.head_node
        prev_node = No

n1 = LinkedList()
n1.insert_new_node(3)
n1.insert_new_node(5)
n1.insert_new_node(9)
n1.insert_new_node(9)
n1.insert_new_node(8)
#print(n1.stringify_list())
n1.remove_node(5)
print("----")
print(n1.stringify_list())
print("----")
n1.remove_all_instances(9)
print("----")
print(n1.stringify_list())