class Note:
    def __init__(self,data):
        self.data = data
        self.next = Note

a = Node("A")
b = Node("B")
c = Node("C")

a.next = b
b.nextn= c

current = a
while current:
    print(f"Node @ {id(current)} | Data:{current.data} | Next:{id(current.next) if current.next else None}")

