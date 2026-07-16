from collections import deque   #simulasi antrian

antrian = deque(["Laporan", "Foto", "Tugas"])

print("\nAntrian :", list(antrian))
while antrian:
    cetak = antrian.popleft()     #mengambil elemen dari antrian
    print("Cetak :", cetak, "| Sisa:", list(antrian))
