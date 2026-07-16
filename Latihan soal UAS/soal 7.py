# Mendefinisikan kelas Node untuk menyimpan data dan pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Mendefinisikan kelas Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Fungsi untuk menambahkan elemen di belakang (Tail)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Fungsi untuk menambahkan elemen di depan (Head)
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Fungsi untuk menampilkan elemen dari Depan ke Belakang (Forward)
    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Maju :", " <-> ".join(elements))

    # Fungsi untuk menampilkan elemen dari Belakang ke Depan (Reverse)
    def display_reverse(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("Mundur :", " <-> ".join(elements))

# --- Eksekusi Program ---
dll = DoublyLinkedList()

# Menambahkan elemen di belakang
dll.append(3)
dll.append(2)

# Menambahkan elemen di depan
dll.prepend(1)
dll.prepend(3)

# Menampilkan hasil
dll.display_forward()
dll.display_reverse()