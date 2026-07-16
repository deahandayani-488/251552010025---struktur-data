# Inisialisasi List Awal
original_list = [1, 2, 3, 4, 5]
stack = [] # Stack dalam Python bisa diwakili oleh list kosong

print("List Asli:", original_list)

# Proses Push (Memasukkan elemen list ke dalam Stack)
for item in original_list:
    stack.append(item)

# Proses Pop (Mengeluarkan elemen dari Stack untuk membuat list baru yang terbalik)
reversed_list = []
while len(stack) > 0:
    reversed_list.append(stack.pop()) # .pop() akan mengambil elemen paling belakang (atas)

# Output
print("List Balik :", reversed_list)