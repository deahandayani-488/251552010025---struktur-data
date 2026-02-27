kontak = {'Fadhil': '08123456789', 'Andi': '08234567890'}
print("Nomor Fadhil:", kontak.get('Fadhil'))
print("Nomor yang tidak ada:", kontak.get('cici', 'tidak ditemukan'))
