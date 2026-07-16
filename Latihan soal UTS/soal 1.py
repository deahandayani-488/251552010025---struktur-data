#mencari nilaiterbesar dan terkecil dalam sebuah list
Angka = [34,7,23,32,5,62]
terbesar = Angka [0]
terkecil = Angka [0]

for i in Angka:
    if i > terbesar:
        terbesar = i
    if i < terkecil: 
        terkecil = i
        
print ("terbesar =", terbesar )
print ("terkecil =", terkecil)
