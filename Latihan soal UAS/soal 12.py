from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")

print("Queue setelah enqueue:", queue)

# Dequeue satu kali
hapus = queue.popleft()
print("Dequeued:", hapus)

print("Queue setelah dequeue:", queue)