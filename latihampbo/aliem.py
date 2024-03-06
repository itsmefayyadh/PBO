class DataBuku:

    def __init__ (self, buku, genre, pengarang, tahun_terbit):
        self.buku = buku
        self.genre = genre
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.list_buku = []

    def tambah_buku (self, buku_baru):
        self.list_buku.append(buku_baru)
        print("Data telah ditambahkan\n")

    def lihat_list (self):
        # print(self.lihat_list)
        for data in self.list_buku:
            print(data.buku, data.genre, data.pengarang, data.tahun_terbit)
            print("\n")


jumlah_buku = int(input("Masukkan jumlah buku mula-mula : "))

start = True
while start != False:
    print("Toko Buku Serba Ada\n1. Tambah data buku\n2. Lihat list buku\n3. Modifikasi buku lama\n4. Hapus buku lama")
    print("5. Keluar program")
    pilih = int(input("Masukkan nomor inputan : "))
    print("\n")

    if pilih == 1:
        buku = input("Masukkan Nama Buku : ")
        genre = input("Masukkan Genre Buku : ")
        pengarang = input("Masukkan Nama Pengarang : ")
        tahun_terbit = input("Masukkan Tahun Terbit : ")
        
        buku = DataBuku(buku, genre, pengarang, tahun_terbit)
        buku.tambah_buku(buku)

    elif pilih == 2:
        buku.lihat_list()

        
    elif pilih != 5:
        continue
    elif pilih == 5:
        print("Terima kasih telah menggunakan program ini")
        break