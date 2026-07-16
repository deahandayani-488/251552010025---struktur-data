def counting_sort(arr):
    maksimum = max(arr)

    count = [0] * (maksimum+1)

    for angka in arr:
        count[angka] += 1

    hasil = []

    for i in range(len(count)):
        hasil += [i] * count[i]

    print("Array asli:", arr)
    print("Counting array:", count)
    print("Hasil sort:", hasil)


data = [4, 2, 2, 8, 3, 3, 1]

counting_sort(data)