# Database pengguna sederhana
users = {
    "Fadhil": "password123",
    "Anya": "admin456",
    "Budi": "dev789"
}

# login check
username = "Fadhil"
password = "password123"


if username in users and users[username] == password:
    print("login berhasil!")
else:
    print("Username atau password salah.")
