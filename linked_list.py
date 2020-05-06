class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data) -> None:
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        
    def ins_pos(self, old_node, new):
        new_node = Node(new)
        new_node.next = old_node.next
        old_node.next = new_node

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = new_node

    def delete(self, data) -> None:
        temp = self.head
        """If given data is in first position"""
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def delele_pos(self, position):
        temp = self.head
        if temp is not None:
            if position == 0:
                self.head = temp.next
                temp = None
                return

        """Find prev_node"""
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if ((temp is None) or (temp.next is None)):
            return 

        next = temp.next.next

        temp.next = None
        temp.next = next
        

    def display(self) -> str:
        temp = self.head
        while(temp):
            print(str(temp.data)+'->', end='')
            temp = temp.next
    


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(15)
    sec = Node(67252)
    third = Node(631)
    ll.head.next = sec
    sec.next = third
    ll.push(0)
    ll.ins_pos(third, 12)
    ll.display()
    print("\n")
    ll.append(99)
    ll.delete(12)
    ll.delele_pos(2)
    print(ll.display())
