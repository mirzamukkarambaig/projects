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

    def __len__(self) -> int:
        lenght = 0
        temp = self.head

        while temp is not None:
            lenght += 1
            temp = temp.next
        
        return lenght

    def getNumber(self) -> float:
        temp = self.head
        length = len(list1)

        multiplier = 10 ** (length - 1)
        number = 0

        while temp:
            number += temp.data * multiplier
            multiplier //= 10
            temp = temp.next

        return number



def multiply(list1: Linkedlist, list2: Linkedlist) -> float:
    multiplicant1 = list1.getNumber()
    multiplicant2 = list2.getNumber()

    return multiplicant1 * multiplicant2

list1 = Linkedlist()
list2 = Linkedlist()

list1.append(1)
list1.append(2)
list1.append(0)

list2.append(2)
list2.append(1)
list2.append(4)

print(multiply(list1, list2))
