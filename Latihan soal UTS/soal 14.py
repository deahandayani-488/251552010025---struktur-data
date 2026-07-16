class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        baru = Node(data)

        if not self.head:
            self.head = baru
            return

        sekarang = self.head

        while sekarang.next:
            sekarang = sekarang.next

        sekarang.next = baru

    def tampil(self):
        sekarang = self.head

        while sekarang:
            print(sekarang.data, end="->")
            sekarang = sekarang.next

        print ("none")

    def delete(self, nilai):

        sekarang =self.head

        if sekarang and sekarang.data == nilai:
            self.head = sekarang.next
            return

        sebelumnya = None

        while sekarang and sekarang.data != nilai:
            sebelumnya = sekarang
            sekarang = sekarang.next

        if sekarang:
            sebelumnya.next

ll = LinkedList()

for i in [10, 20, 30, 40, 50]:
    ll.append(i)

print("Sebelum:")
ll.tampil()

ll.delete(30)

print("Sesudah:")
ll.tampil()
