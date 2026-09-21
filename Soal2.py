a = int(input("masukkan bilangan pertama: "))
b = int(input("masukkan bilangan kedua: "))
c = int(input("masukkan bilangan ketiga: "))

if a >= b and a >=c:
    terbesar = a
elif b >= a and b >=c:
    terbesar = b
else:
    terbesar = c
print("bilangan terbesar: ", terbesar)
