Input = "algoritma"   #membalikan sebuah string menggunakan stack
stack = []

for ch in Input:   #melakukan perulangan 
    stack.append(ch) #menyimpan karakter

terbalik = ""
while stack:
    terbalik += stack.pop()

print("\nOriginal :", Input)
print("Terbalik :", terbalik)