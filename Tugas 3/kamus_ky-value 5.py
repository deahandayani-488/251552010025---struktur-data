# Database pengguna
user = {
    "Fadhli": "password123",
    "Anya": "admin456",
    "Abdu": "dev789"
}

# Daftar login yang ingin dicek
login_attempts = [
    ("Fadhli", "password123"),
    ("katanyan", "salahpassword"),
    ("Abdu", "dev789"),
    ("Budi", "abc123")
]

# Cek semua login
for username, password in login_attempts:
    if username in user and user[username] == password:
        print(f"Login {username}: BERHASIL")
    else:
        print(f"Login {username}: GAGAL - Username atau password salah")
