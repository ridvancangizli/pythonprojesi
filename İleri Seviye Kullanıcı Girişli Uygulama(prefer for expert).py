import time
import random as r

print("Merhaba Uygulamamıza Hoşgeldiniz")
kullanıcı = "rıdvancangizli"
sifre = "rıd"
while True:
    kullanıcıadı = input("Lütfen Kullanıcı Adınızı Giriniz:")
    kullanıcısifre = input("Lütfen Şifrenizi Giriniz:") 
    if kullanıcıadı == kullanıcı and kullanıcısifre == sifre:
        print("İşleminiz Gerçekleştiriliyor.")
        time.sleep(1)
        for i in range(3,0,-1):
            time.sleep(1)
            print("Saniye Kaldı",i)
        time.sleep(1)
        print("Başarılı Bir Şekilde Giriş Yaptınız Sayın:  " + kullanıcıadı + "!")
        time.sleep(1)
        while True:
            time.sleep(2)
            print("Uygulama Yükleniyor...")
            time.sleep(2)
            print("""
            Çarpma İçin = 1
            Çıkarma İçin = 2
            Toplama İçin = 3
            Bölme İçin = 4
            Faktoriyel Hesaplama İçin = 5
            Sayı Tahmin Oyunu İçin = 6
            Asal Sayı Bulma = 7
            
            Çıkmak İçin = q  """)
            secim = input("Merhaba Sayın  " + kullanıcıadı + " Lütfen Yapmak İstediğini İşlemi Giriniz:")
            
            if secim == "q":
                time.sleep(2)
                print("Çıkış Yapılıyor")
                time.sleep(1)
                break
            elif secim == "1":
                kutu = int(input("Lütfen İlk Değeri Giriniz:"))
                kutu2 = int(input("Lütfen İkinci Değeri Giriniz:")) 
                çarpma = kutu * kutu2
                time.sleep(1)
                print("İşleminiz Gerçekleştiriliyor !",kullanıcıadı)
                print("Çarpma Sonucunuz", "=" , çarpma)
            
            elif secim == "2":
                kutu = int(input("Lütfen İlk Değeri Giriniz:"))
                kutu2 = int(input("Lütfen İkinci Değeri Giriniz:")) 
                çıkarma = kutu - kutu2
                time.sleep(1)
                print("İşleminiz Gerçekleştiriliyor !",kullanıcıadı)
                print("Çıkarma Sonucunuz", "=" , çıkarma)
            
            elif secim == "3":
                kutu = int(input("Lütfen İlk Değeri Giriniz:"))
                kutu2 = int(input("Lütfen İkinci Değeri Giriniz:")) 
                toplama = kutu + kutu2
                time.sleep(1)
                print("İşleminiz Gerçekleştiriliyor !",kullanıcıadı)
                print("Toplama Sonucunuz", "=" , toplama)
                
            elif secim == "4":
                kutu = int(input("Lütfen İlk Değeri Giriniz:"))
                kutu2 = int(input("Lütfen İkinci Değeri Giriniz:")) 
                bölme = kutu / kutu2
                time.sleep(1)
                print("İşleminiz Gerçekleştiriliyor !",kullanıcıadı)
                print("Bölme Sonucunuz", "=" , bölme)
                
            elif secim == "5":
                sayi = int(input("Lütfen Hesaplamak İstediğiniz Sayıyı Giriniz:"))
                faktoriyel = 1
                for hesaplayıcı in range(sayi):
                    faktoriyel = faktoriyel * (hesaplayıcı+1)
                    time.sleep(1)
                print("Merhaba Sayın", kullanıcıadı , "Faktoriyel Sonucunuz:", faktoriyel)
                        
            elif secim == "6":
                karışık = r.randint(1,60)
                hak_sahibi = 5            
                while True:
                
                    onaylama = int(input("Lütfen Bir Sayı Tahmin Edin:"))
                    
                    if onaylama == karışık:
                        print("Doğru Bildiniz!")
                        break
                            
                    if onaylama < karışık:
                        print("Daha Büyük Giriniz")
                        print("-----------------------")
                        hak_sahibi = hak_sahibi - 1
                        print("Hakkınız Kaldı",hak_sahibi)
                        if hak_sahibi == 0:      
                            break
                            
                        
                    if onaylama > karışık:
                        print("Daha Küçük")
                        print("-----------------------")
                        hak_sahibi = hak_sahibi - 1
                        print("Hakkınız Kaldı",hak_sahibi)
                        if hak_sahibi == 0:
                            break
            elif secim == "7":
                
                def ekstra(fonk):
    
                    def ekstra_ozellik():
                        print("Mükemmel Sayılar...")
                        for sayı in range(1,101):
                            toplam = 0
                            i = 1
                            while (i < sayı):
                                if (sayı % i == 0):
                                    toplam += i
                                i +=1
                            if (toplam == sayı):
                                print(sayı)
                        fonk()
                                
                    return ekstra_ozellik
                    
                
                
                @ekstra
                def asal_sayılar():
                    print("Asal Sayılar...")
                    for sayı in range(2,1001):
                        i = 2 
                        say = 0
                        while (i < sayı):
                            if (sayı % i == 0):
                                say += 1
                            i += 1
                        if (say == 0):
                            print(sayı)
                            
                asal_sayılar() 
                
            
    elif (kullanıcıadı != kullanıcı and kullanıcısifre == sifre):
        print("İşleminiz Gerçekleştiriliyor")
        time.sleep(1)
        for i in range(3,0,-1):
            time.sleep(1)
            print("Saniye Kaldı",i)
        time.sleep(1)
        print("Kullanıcı Adınız Hatalı Lütfen Tekrar Deneyiniz", "Sayın: '" + kullanıcıadı + "'")
    elif kullanıcıadı == kullanıcı and kullanıcısifre != sifre:
        print("İşleminiz Gerçekleştiriliyor.")
        time.sleep(1)
        for i in range(3,0,-1):
            time.sleep(1)
            print("Saniye Kaldı",i)
        time.sleep(1)
        print("Şifreniz Hatalı Lütfen Tekrar Deneyiniz Sayın:"   + kullanıcısifre + "!")
        time.sleep(1)
    else:
        print("İşleminiz Gerçekleştiriliyor.")
        time.sleep(1)
        for i in range(3,0,-1):
            time.sleep(1)
            print("Saniye Kaldı",i)
        time.sleep(1)
        print("Her İki Bilginizde Hatalı Lütfen Tekrar Deneyiniz" , kullanıcıadı, "=", kullanıcısifre,"!")
        time.sleep(1)
        
        
        
        
        
    
    
        
    

