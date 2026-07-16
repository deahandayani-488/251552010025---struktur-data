#menghapus elemen duplikat dalam sebuah list
data = [3,1,4,1,5,9,2,6,5,3,5]

angka =[]
for i in data:
    if i not in angka:     
        angka.append(i)
print (angka)



