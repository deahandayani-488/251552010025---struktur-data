#menghitung frekuensi kemunculan setiap kata dalam sebuah kalimat
kalimat = 'apel, jeruk, apel, mangga, jeruk, apel'
data = kalimat.split(', ') #memisahkan kata dalam list
hasil = []

for item in data:
    if item not in hasil:
        hasil.append(item) 

print(hasil)