def toStr (n,m):
    ConvertString = "0123456789ABCDEF"
    if n < m:
        return ConvertString[n]
    else:
        return toStr(n // m,m) + ConvertString[n % m]
    
Angka1 = int(input("Angka 1 :"))
Angka2 = int(input("Angka 2 :"))
print(toStr(Angka1,Angka2))