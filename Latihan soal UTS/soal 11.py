desimal  = 42
stack = []

while desimal > 0:              #mengulang proses pembagian
    sisa = desimal % 2          #untuk mengitung sisa pebagian 2 untuk menghasilkan 1/0
    stack.append(sisa)          #menyimpan pembagian 2
    desimal = desimal // 2

biner = ""

while stack:                        #mengembalikan urutan angka 
    biner += str(stack.pop())       #selama stack masih memiliki data ambil data terakhir dengan pop()

print("Biner:", biner)