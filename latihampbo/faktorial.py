def faktorial(n):
    if (n <= 1): # kasus basis
        return 1
    else: # pemanggilan rekursif
        return n * faktorial(n-1)
 
n = int(input("Masukkan angka :"))
print(faktorial(n))

daftar_kegiatan = ["sarapan", "mandi","belajar"]

# variasi 1
for kegiatan in daftar_kegiatan:
    print(kegiatan)
# variasi 2
for i in range(len(daftar_kegiatan)):
    print(daftar_kegiatan[i])

ini_tupel = ("objek",)
print(type(ini_tupel)) # merupakan tupel
ini_bukan_tupel_1 = ("objek")
print(type(ini_bukan_tupel_1)) # merupakan string
ini_bukan_tupel_2 = (100)
print(type(ini_bukan_tupel_2)) # merupakan int