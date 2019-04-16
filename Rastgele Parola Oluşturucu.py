import random
import string

açılış = print("Hoş Geldiniz Bu Rastgele Parola Oluşturucudur Seçimlerinize Göre Size Uygun Parola Oluşturacaktır..!!!")
uyarı = print("Parolanızı Kaydetmeyi Unutmayın Program Parolanızı Kaydetmeyecek....!!!!!")
uyarı2 = print("Seçimlerinizi Lütfen Büyük Harflerle Yazınız..!!!")
Sayı = input("Hoşgeldiniz. Parolanızın içerisinde sayı olsun mu? [E/H]")
Harf = input("Parolanızın içerisinde harf olsun mu? [E/H]")
ÖzelKarakter = input("Parolanızın içerisinde özel karakter olsun mu? [E/H]")
Uzunluk = int(input("Parolanız kaç karakter olsun ?"))

def randomStringwithDigitsAndSymbols(stringLength = Uzunluk ):
    if Sayı == "E":
        password_characters = string.digits
    if Harf == "E":
        password_characters = string.digits + string.ascii_letters
    if ÖzelKarakter == "E":
        password_characters = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))
print ("Şifreniz : ", randomStringwithDigitsAndSymbols(Uzunluk) )

#AloneAngels Tarafından Python Proje Ödevi İçin Yazılmıştır...!!!!