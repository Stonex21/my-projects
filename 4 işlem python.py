kulanici_adi = int(input("1.sayıyı giriniz:"))
kulanici_adi1 = int(input("2.sayıyı giriniz:"))
islem = input("Yapılacak işlemi giriniz:")
if islem == 'toplama':
      print(kulanici_adi+kulanici_adi1)

elif islem == "çıkartma":
      print(kulanici_adi-kulanici_adi1)

elif islem == "çarpma":
      print(kulanici_adi*kulanici_adi1)

elif islem == "bölme":
      print(kulanici_adi//kulanici_adi1)

else: 
        print("işlem başarısız")
