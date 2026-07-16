#mencari anggota yang memiliki 2 eskul dan 1 eskul
basket = {'andi', 'budi', 'cici','deni'}
futsal = {'budi', 'deni', 'eko', 'fani'}

dua_eskul = basket.intersection(futsal)  
satu_eskul = basket.symmetric_difference(futsal)  

print("Ikut 2 eskul:", dua_eskul)
print("Ikut 1 eskul:", satu_eskul)



