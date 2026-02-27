user = {"name": "Fadhli", "ege": 27}

# Menggunakan get agar aman dari keyerror
email = user.get("email", "Email belum tersedia")
print(email)

# Menambahkan key jika belum ada dengan setdefault
user.setdefault("email", "Fadhli@example.com")

# Update data
user.update({"age": 28,  "role": "Devops"})

# Menghapus key
age = user.pop("age")

# Menampilkan semua key dan values
print(user.keys())
print(user.values())

# Menyalin dictionary
user_copy = user.copy()
print(user_copy)

print(user)
print(user_copy)
