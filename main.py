from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd

def main():
    try:
        # Personel nesneleri oluşturma
        personel1 = Personel(1, "Umut", "Özbek", "Yönetim", 5000)
        personel2 = Personel(2, "Eren", "Demir", "Muhasebe", 4500)

        print(personel1)
        print(personel2)

        # Doktor nesneleri oluşturma
        doktor1 = Doktor(3, "Kaan", "Kara", "Cerrahi", 8000, "Ortopedi", 10, "Acıbadem")
        doktor2 = Doktor(4, "Esma", "Vural", "Kardiyoloji", 7500, "Kardiyolog", 12, "Medicana")
        doktor3 = Doktor(5, "Fatma", "Taş", "Pediatri", 7200, "Çocuk Doktoru", 8, "MedicalPark")

        print(doktor1)
        print(doktor2)
        print(doktor3)

        # Hemşire nesneleri oluşturma
        hemsire1 = Hemsire(6, "Zeynep", "Öztürk", "Yoğun Bakım", 4000, 40, "Yoğun Bakım Hemşiresi", "Acıbadem")
        hemsire2 = Hemsire(7, "Merve", "Yıldız", "Acil", 4200, 35, "Acil Servis Hemşiresi", "Medicana")
        hemsire3 = Hemsire(8, "Elif", "Çelik", "Ameliyathane", 4500, 45, "Ameliyathane Hemşiresi", "MedicalPark")

        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        # Hasta nesneleri oluşturma
        hasta1 = Hasta(9, "Akgün", "Taşkın", "1980-05-10", "Grip", "Dinlenme ve İlaç")
        hasta2 = Hasta(10, "Canan", "Kara", "1990-03-22", "Kırık", "Alçı ve Fizik Tedavi")
        hasta3 = Hasta(11, "Deniz", "Çınar", "2000-11-30", "Enfeksiyon", "Antibiyotik Tedavisi")

        print(hasta1)
        print(hasta2)
        print(hasta3)

        # Pandas DataFrame oluşturma
        data = {
            "personel_no": [personel1.get_personel_no(), personel2.get_personel_no(),
                            doktor1.get_personel_no(), doktor2.get_personel_no(), doktor3.get_personel_no(),
                            hemsire1.get_personel_no(), hemsire2.get_personel_no(), hemsire3.get_personel_no(),
                            hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
            "ad": [personel1.get_ad(), personel2.get_ad(),
                   doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(),
                   hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(),
                   hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
            "soyad": [personel1.get_soyad(), personel2.get_soyad(),
                      doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(),
                      hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(),
                      hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
            "departman": [personel1.get_departman(), personel2.get_departman(),
                          doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(),
                          hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(),
                          None, None, None],
            "maas": [personel1.get_maas(), personel2.get_maas(),
                     doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(),
                     hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(),
                     None, None, None],
            "uzmanlik": [None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(),
                         None, None, None, None, None, None],
            "deneyim_yili": [None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(),
                             None, None, None, None, None, None],
            "hastane": [None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(),
                        hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane(),
                        None, None, None],
            "calisma_saati": [None, None, None, None, None,
                              hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(),
                              None, None, None],
            "sertifika": [None, None, None, None, None,
                          hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(),
                          None, None, None],
            "hasta_no": [None, None, None, None, None,
                         None, None, None, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
            "dogum_tarihi": [None, None, None, None, None,
                             None, None, None, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
            "hastalik": [None, None, None, None, None,
                         None, None, None, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
            "tedavi": [None, None, None, None, None,
                       None, None, None, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()]
        }

        df = pd.DataFrame(data)
        print(df)
         # Boş olan değişken değerleri için 0 atayınız
        df.fillna(0, inplace=True)
        print("Boş değerler 0 olarak atandı:")
        print(df)

        # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplayınız
        doktor_grup = df[df["uzmanlik"] != 0].groupby("uzmanlik").size()
        print("\nDoktorların uzmanlık alanlarına göre dağılımı:")
        print(doktor_grup)

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulunuz
        deneyimli_doktorlar = df[(df["deneyim_yili"] > 5) & (df["deneyim_yili"] != 0)].shape[0]
        print("\n5 yıldan fazla deneyime sahip doktor sayısı:", deneyimli_doktorlar)

        # Hasta adına göre DataFrame’i alfabetik olarak sıralayınız
        df_sorted_by_name = df.sort_values("ad")
        print("\nHasta adına göre alfabetik olarak sıralanmış DataFrame:")
        print(df_sorted_by_name)

        # Maaşı 7000 TL üzerinde olan personelleri bulunuz
        high_salary_personnel = df[df["maas"] > 7000]
        print("\nMaaşı 7000 TL üzerinde olan personeller:")
        print(high_salary_personnel)

        # Yeni DataFrame oluşturma
        new_df = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
        print("\nYeni DataFrame:")
        print(new_df)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
