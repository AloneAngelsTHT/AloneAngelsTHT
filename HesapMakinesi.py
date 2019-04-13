print("""
	AloneAngels Tarafından Yazılmıştır
=====================
[1]Toplama
[2]Çıkarma
[3]Çarpma
[4]Bölme
=====================
	""")

seçim = input("Yapılacak İşlemi Seçiniz[1,2,3,4] : ")

if seçim == "1":
	sayi1 = input("1.Sayıyı Giriniz : ")
	sayi1x = float(sayi1)
	sayi2 = input("2.Sayıyı Giriniz : ")
	sayi2x = float(sayi2)
	print("{} Sayısı İle {} Sayısının Toplamı = {}".format(sayi1x,sayi2x,sayi1x+sayi2x))

elif seçim == "2":
	sayi1 = input("1.Sayıyı Giriniz : ")
	sayi1x = float(sayi1)
	sayi2 = input("2.Sayıyı Giriniz : ")
	sayi2x = float(sayi2)
	print("{} Sayısı İle {} Sayısının Farkı = {}".format(sayi1x,sayi2x,sayi1x-sayi2x))

elif seçim == "3":
	sayi1 = input("1.Sayıyı Giriniz : ")
	sayi1x = float(sayi1)
	sayi2 = input("2.Sayıyı Giriniz : ")
	sayi2x = float(sayi2)
	print("{} Sayısı İle {} Sayısının Çarpımı = {}".format(sayi1x,sayi2x,sayi1x*sayi2x))

elif seçim == "4":
	sayi1 = input("1.Sayıyı Giriniz : ")
	sayi1x = float(sayi1)
	sayi2 = input("2.Sayıyı Giriniz : ")
	sayi2x = float(sayi2)
	print("{} Sayısı İle {} Sayısının Sonucu = {}".format(sayi1x,sayi2x,sayi1x/sayi2x))

else :
	print("Hata Lütfen Verilen Değerler İçerisinde Seçim Yapınız....!!!!")
#AloneAngels Tarafından Python Proje Ödevi Olarak Hazırlanmıştır......