# Inisialisasi Set A dan Set B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 1. Union (Gabungan)
union = A | B  # Bisa juga pakai A.union(B)

# 2. Intersection (Irisan)
intersection = A & B  # Bisa juga pakai A.intersection(B)

# 3. Difference (Selisih A - B)
difference = A - B    # Bisa juga pakai A.difference(B)

# 4. Symmetric Difference (Selisih Simetris)
symmetric_diff = A ^ B # Bisa juga pakai A.symmetric_difference(B)

# Output
print("Union (A | B)     :", union)
print("Intersection (A&B):", intersection)
print("Difference (A - B):", difference)
print("Symmetric Diff (A^B):", symmetric_diff)