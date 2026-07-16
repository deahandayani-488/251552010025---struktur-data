orang = ['Ali', 'Budi', 'Cici', 'Deni', 'Eka']
k = 3

index = 0

while len(orang) > 1:
    index = (index + k - 1) % len(orang)        #permainan melingkar % untuk membuat index len untuk kembali melewati list

    keluar = orang.pop(index)                   #pop menghapus giliran yang mencapai k
    print("keluar:", keluar)

print("Pemenang:", orang[0])