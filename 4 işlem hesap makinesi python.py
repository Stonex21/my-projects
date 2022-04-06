try:

    kulanici_adi = float(input("1.sayıyı giriniz:"))
    kulanici_adi1 = float(input("2.sayıyı giriniz:"))
    islem = input("Yapılacak işlemi giriniz:")
    if islem == 'toplama' or islem == "Toplama":
          print(kulanici_adi+kulanici_adi1)

    elif islem == "çıkartma" or islem == "Çıkartma":
      print(kulanici_adi-kulanici_adi1)

    elif islem == "çarpma" or islem == "Çarpma" :
       print(kulanici_adi*kulanici_adi1)

    elif islem == "bölme" or islem == "Bölme":  
          print(kulanici_adi//kulanici_adi1)

    else: 
         print("işlem başarısız")
         
except:
    print("!Lütfen sayı giriniz!")