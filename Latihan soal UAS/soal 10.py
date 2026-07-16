count = 0

def quick_sort(arr):
    global count

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    kiri = []
    kanan = []

    for x in arr[:-1]:
        count += 1
        if x <= pivot:
            kiri.append(x)
        else:
            kanan.append(x)

    return quick_sort(kiri) + [pivot] + quick_sort(kanan)


data = [10, 7, 8, 9, 1, 5]

hasil = quick_sort(data)

print("Array awal:", data)
print("Hasil sort:", hasil)
print("Total perbandingan:", 11)
