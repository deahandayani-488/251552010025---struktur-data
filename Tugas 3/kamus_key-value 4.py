# Database pengguna
users = {
    "Fadhil": "passsword123",
    "Anya": "admin456",
    "Budi": "dev789"
}

print("=== Login Manual ===")
input_username = input("masukkan username: ")
input_password = input("masukkan password: ")

if input_username in users and users[input_username] == input_password:
    print(f"Login {input_username}: BERHASIL")
else:
    print(f"Login {input_username}: GAGAL - Username atau password salah")
