from random import randint

sayiTahmin = randint(1, 100)

tahminEdilen = -1

while sayiTahmin != tahminEdilen:
    tahminEdilen = int(input("Bir sayi giriniz : "))
    if sayiTahmin > tahminEdilen:
        print("Yükselt")
    elif sayiTahmin < tahminEdilen:
        print("Düşür")
    else:
        print("Dogru Tahmin")
