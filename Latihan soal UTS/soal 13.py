data = {
    'andi': 88,
    'budi': 72,
    'cici': 65,
    'deni': 91,
    'eka': 68,
    'fani': 75
}

A = []
B = []
C = []

for nama, nilai in data.items():            #mengambil nama dan nilai

#memilih kategori nilai
    if nilai >= 85:
        A.append(nama)

    elif nilai >= 70:
        B.append(nama)

    else:
        C.append(nama)

print("A:", A)
print("B:", B)
print("C:", C)
