angka = [2, 1, 5, 1, 3, 2]  #panjang yg memiliki jumlah max
k = 3

jumlah_maksimum = 0
sublist_terbaik= []

#menggeser sub list sepanjang k
for i in range(len(angka) - k + 1):
    sublist = angka[i:i+k]
    jumlah = sum(sublist)                #menghitung total setiap list

    if jumlah > jumlah_maksimum:          #mencari jumlah terbesar
        jumlah_maksimum = jumlah
        sublist_terbaik = sublist

print("Sub list terbaik:", sublist_terbaik)
print("Jumlah maksimum:", jumlah_maksimum)
