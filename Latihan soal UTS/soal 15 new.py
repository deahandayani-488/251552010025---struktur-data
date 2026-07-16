class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
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
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next            #tidak boleh mehilangkan node selanjutnya
            current.next = prev
            prev = current
            current = next_node             #untuk membalikan arah node
        self.head = prev

# Menjalankan kode
ll = LinkedList()
for i in [1,2,3,4,5]:
    ll.append(i)

print("Sebelum:")
ll.tampil()

ll.reverse()

print("Sesudah:")
ll.tampil()
