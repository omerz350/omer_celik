class Kutuphane:
    def __init__(self):
        self.dosya_adi = "kitaplar.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def __exit__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        with open(self.dosya_adi, "r") as f:
            kitaplar = f.readlines()
            for kitap in kitaplar:
                kitap_adi, yazar, yayin_yili, sayfa_sayisi = kitap.strip().split(",")
                print(f"Kitap adı: {kitap_adi}, Yazar: {yazar}, Yayın Yılı: {yayin_yili}, Sayfa Sayısı: {sayfa_sayisi}")

    def kitap_ekle(self):
        kitap_adi = input("Kitap adını girin: ")
        yazar = input("Kitap yazarını girin: ")
        yayin_yili = input("Yayın yılını girin: ")
        sayfa_sayisi = input("Sayfa sayısını girin: ")

        with open(self.dosya_adi, "a+") as f:
            f.write(f"{kitap_adi},{yazar},{yayin_yili},{sayfa_sayisi}\n")
        print("Kitap başarıyla eklendi!")

    def kitap_sil(self):
        kitap_adi = input("Silmek istediğiniz kitabın başlığını girin: ")

        with open(self.dosya_adi, "r") as f:
            kitaplar = f.readlines()

        with open(self.dosya_adi, "w") as f:
            for kitap in kitaplar:
                if kitap_adi not in kitap:
                    f.write(kitap)
        print("Kitap başarıyla silindi!")

def ana_program():
    kutuphane = Kutuphane()

    while True:
        print("*** MENÜ ***")
        print("1) Kitapları Listele")
        print("2) Kitap Ekle")
        print("3) Kitap Sil")
        print("q) Çıkış")
        secim = input("Lütfen seçiminizi yapın (1/2/3/q): ")

        if secim == "1":
            kutuphane.kitaplari_listele()
        elif secim == "2":
            kutuphane.kitap_ekle()
        elif secim == "3":
            kutuphane.kitap_sil()
        elif secim.lower() == "q":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1, 2, 3 veya q girin.")

if __name__ == "__main__":
    ana_program()