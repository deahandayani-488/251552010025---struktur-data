angka = [1, 2, 3, 4, 6, 8, 9]   #cari semua pasangan bilangan
target = 10

kiri = 0
kanan = len(angka) - 1  #mengambil variabel khusus
pasangan = []

while kiri < kanan:
    jumlah = angka[kiri] + angka[kanan]
    if jumlah == target:
        pasangan.append((angka[kiri], angka[kanan]))
        kiri += 1
        kanan -= 1
    elif jumlah < target:
        kiri += 1
    else:
        kanan -= 1

print("\nPasangan yang jumlahnya 10:")
for p in pasangan:     #menampilkan pasangan
    print(p) 