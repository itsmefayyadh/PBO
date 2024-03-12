import random


class bokap:
    def __init__ (self,goldar):
        self.goldar = goldar

class nyokap:
    def __init__ (self,goldar):
        self.goldar = goldar

class anak:
    def __init__(self, bokap, nyokap):
        self.bokap_goldar = bokap.goldar
        self.nyokap_goldar = nyokap.goldar
        self.allele1 = random.choice([bokap.goldar[0], nyokap.goldar[1]])
        self.allele2 = random.choice([bokap.goldar[1], nyokap.goldar[0]])
        
    def penggabungan(self):
        tipe_darah = self.allele1 + self.allele2
        if tipe_darah == 'AA':
            return 'A'
        elif tipe_darah == 'AB':
            return 'AB'
        elif tipe_darah == 'AO':
            return 'A'
        elif tipe_darah == 'BB':
            return 'B'
        elif tipe_darah == 'BO':
            return 'B'
        else:
            return 'O'


bokap_goldar = input("Masukkan Golongan Darah Ayah : ")
nyokap_goldar = input("Masukkan Golongan Darah Ibu : ")

Bokap = bokap(bokap_goldar)
Nyokap = nyokap(nyokap_goldar)
Anak = anak(Bokap, Nyokap)

print("Golongan Darah Ayah: ", Bokap.goldar)
print("Mother's blood type:", Nyokap.goldar)
print("Child's blood type:", Anak.penggabungan())