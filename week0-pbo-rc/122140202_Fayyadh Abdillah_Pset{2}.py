kumpulan_nilai = dict()
jml = int(input("Enter the number of students to display grades: "))

# for(int i = 0; i < jml; i++)
for i in range(jml):
    nama = input("Masukkan nama: ")
    nilai = input("Masukkan nilai: ")
    kumpulan_nilai[nama] = nilai

print(kumpulan_nilai)
