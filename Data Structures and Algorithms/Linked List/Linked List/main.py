class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp  
            self.tail = temp

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    def iterative_reverse(self):
        previous = None
        current = self.head
        nextptr = None

        while(current is not None):
            nextptr = current.next
            current.next = previous

            previous = current
            current = nextptr

        self.head = previous
        
linkedlist = Linkedlist()

linkedlist.append(1)
linkedlist.append("Mukkaram")
linkedlist.append(56.21)
linkedlist.append(True)

linkedlist.print_list()

linkedlist.reverse()

linkedlist.print_list()