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

    def print(self) -> None:
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

    def remove_duplicates(self):
        temp = self.head
        unique = dict()
        i = 0

        while temp is not None:
            if temp.next.data in unique:
                temp.next = temp.next.next
            else:
                unique[i] = temp.data
                i += 1

    def remove_duplicates(self) -> None:
        if not self.head:
            return

        temp = self.head
        unique = set()
        unique.add(temp.data)  

        while temp.next is not None:  
            if temp.next.data in unique:
                temp.next = temp.next.next
            else:
                unique.add(temp.next.data)  
                temp = temp.next  

    def sort_ternary(self):
        count = [0] * 3
        temp = self.head

        while temp is not None:
            if temp.data == 0:
                count[0] += 1
            elif temp.data == 1:
                count[1] += 1
            else:
                count[2] += 1
            
            temp = temp.next

        i = 0
        temp = self.head

        while temp is not None:
            if count[i] == 0:
                i += 1
            else:
                temp.data = i
                count[i] -= 1
                temp = temp.next



list = Linkedlist()

list.append(0)
list.append(2)
list.append(1)
list.append(0)
list.append(2)
list.append(1)
list.append(2)
list.append(1)

list.sort_ternary()

list.print()

