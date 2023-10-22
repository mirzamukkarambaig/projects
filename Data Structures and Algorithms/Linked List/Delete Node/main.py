from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data) -> None:
        temp = Node(data)

        if self.head is None and self.tail is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def print_list(self) -> None:
        temp = self.head

        while temp is not None:
            print(temp.data, end = "->")
            temp = temp.next

        print("None")

    def delete_first(self) -> Optional[str]:
        if self.head is None:
            return "List is Empty"
        self.head = self.head.next
        if self.head is None:
            self.tail = None  


    def delete_last(self) -> Optional[str]:
        if self.head is None:
            return "List is Empty"
        
        if self.head == self.tail:
            self.head = self.tail = None
            return
        
        temp = self.head

        while temp.next is not self.tail:
            temp = temp.next

        temp.next = None
        self.tail = temp

    def delete_at_position(self, position) -> None:
        if not self.head or position < 0:
            return 

        if position == 0:
            self.delete_first()
            return

        temp = self.head
        for i in range(position - 1):
            if not temp.next:
                return  
            temp = temp.next

        if temp.next:
            if temp.next == self.tail:
                self.tail = temp  
            temp.next = temp.next.next