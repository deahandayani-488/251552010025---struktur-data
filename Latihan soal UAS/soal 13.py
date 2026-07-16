class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tampil(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, nilai):
        temp = self.head

        if temp and temp.data == nilai:
            self.head = temp.next
            return

        while temp.next:
            if temp.next.data == nilai:
                temp.next = temp.next.next
                return
            temp = temp.next


list = LinkedList()

for x in [10,20,30,40,50]:
    node = Node(x)

    if list.head is None:
        list.head = node
    else:
        temp = list.head
        while temp.next:
            temp = temp.next
        temp.next = node


print("Sebelum:", end=" ")
list.tampil()

list.delete(30)

print("Sesudah:", end=" ")
list.tampil()