print("Menyimpan ke file...")

with open('Me.txt', 'w') as f:
    f.write('Nama : Fayyadh Abdillah\n')
    f.write('NIM : 122140202\n')
    f.write('Resolusi Saya di Tahun ini : Nonton konser JKT48')
text = open('Me.txt')

print("Berhasil menyimpan!")
print("Isi file: ")

print(text.read())