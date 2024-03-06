# Definisi kelas hero
class Hero:
    def __init__(self, nama, health, regen_rate, armor, attack):
        self.nama = nama
        self.health = health
        self.regen_rate = regen_rate
        self.armor = armor
        self.attack_power = attack
        self.defense = False
    
    def getName(self):
        return self.nama
    
    def getHealth(self):
        return self.health
    
    def getRegenRate(self):
        return self.regen_rate
    
    def getArmor(self):
        return self.armor
    
    def getAttack(self):
        return self.attack_power

    def doAttack(self, enemy):
        if not self.defense:
            damage_taken = max(0, self.attack_power - enemy.getArmor())
            enemy.health -= damage_taken
            print(f"{self.nama} menyerang {enemy.getName()} dan menyebabkan {damage_taken} damage")
        else:
            print(f"{self.nama} dalam mode pertahanan, serangan tidak menyebabkan kerusakan pada lawan")
        self.displayStatus()
    
    def regen(self):
        self.health += self.regen_rate
        print(f"{self.nama} mendapatkan {self.regen_rate} health dari regen. Total health sekarang: {self.health}")
        self.displayStatus()

    def toggleDefense(self):
        self.defense = not self.defense
        if self.defense:
            print(f"{self.nama} mengaktifkan mode pertahanan")
        else:
            print(f"{self.nama} menonaktifkan mode pertahanan")
        self.displayStatus()

    def displayStatus(self):
        print(f"{self.nama} - Health: {self.health}, Armor: {self.armor}, Attack: {self.attack_power}")

def input_hero_data():
    nama = input("Masukkan nama hero: ")
    health = int(input("Masukkan jumlah health hero: "))
    regen_rate = int(input("Masukkan tingkat regenerasi health hero: "))
    armor = int(input("Masukkan jumlah armor hero: "))
    attack = int(input("Masukkan kekuatan serangan hero: "))
    return Hero(nama, health, regen_rate, armor, attack)

if __name__ == "__main__":
    print("Data Hero Pertama:")
    hero1 = input_hero_data()

    print("\nData Hero Kedua:")
    hero2 = input_hero_data()

    print("\nStatus Awal Hero:")
    hero1.displayStatus()
    hero2.displayStatus()

    turn = 1

    while True:
        print(f"\nGiliran Pemain {turn}:")
        print("\nSilahkan Jalan")
        print("1. Attack")
        print("2. Regen")
        print("3. Active Defense")
        print("4. Keluar")

        choice = int(input("Pilih aksi yang ingin dilakukan: "))
        if choice == 1:
            if turn == 1:
                hero1.doAttack(hero2)
            else:
                hero2.doAttack(hero1)
        elif choice == 2:
            if turn == 1:
                hero1.regen()
            else:
                hero2.regen()
        elif choice == 3:
            if turn == 1:
                hero1.toggleDefense()
            else:
                hero2.toggleDefense()
        elif choice == 4:
            print("Terima kasih telah bermain!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih lagi.")
        turn = 2 if turn == 1 else 1

    print("\nStatus Terakhir Hero:")
    hero1.displayStatus()
    hero2.displayStatus()
