from django.db import models

# Create your models here.

class Kullanici(models.Model):
    ROLLER = [('ogrenci', 'Öğrenci'), ('ogretim_uyesi', 'Öğretim Üyesi'), ('yonetici', 'Yönetici')]

    isim = models.CharField(max_length=100)
    soyisim = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sifre = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROLLER)

    class Meta:
        verbose_name_plural = "Kullanıcılar"

    def __str__(self):
        return f"{self.isim} {self.soyisim}"

class Bolum(models.Model):
    ad = models.CharField(max_length=100)
    kod = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name_plural = "Bölümler"

    def __str__(self):
        return self.ad

class Ders(models.Model):
    ad = models.CharField(max_length=100)
    kod = models.CharField(max_length=20, unique=True)
    haftalik_saat = models.IntegerField()
    ogretim_uyesi = models.ForeignKey(Kullanici, on_delete=models.SET_NULL, null=True)
    bolum = models.ForeignKey(Bolum, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Dersler"

    def __str__(self):
        return f"{self.ad} ({self.kod})"

class Derslik(models.Model):
    STATU = [('NORMAL', 'Normal'), ('LAB', 'Laboratuvar')]
    ad = models.CharField(max_length=50, verbose_name='Sınıf Adı', default='Derslik 1')
    kapasite = models.IntegerField()
    statu = models.CharField(max_length=10, choices=STATU)

    class Meta:
        verbose_name_plural = "Derslikler ve Mevcut"

    def __str__(self):
        return f"{self.ad} ({self.statu})"

class DersProgrami(models.Model):
    GUNLER = [('Pazartesi', 'Pazartesi'), ('Salı', 'Salı'), ('Çarşamba', 'Çarşamba'),
              ('Perşembe', 'Perşembe'), ('Cuma', 'Cuma')]

    SAATLER = [('08:00-09:00', '08:00-09:00'), ('09:00-10:00', '09:00-10:00'),
               ('10:00-11:00', '10:00-11:00'), ('11:00-12:00', '11:00-12:00'), ('12:00-13:00', '12:00-13:00'),
               ('13:00-14:00', '13:00-14:00'),('14:00-15:00', '14:00-15:00'),('15:00-16:00', '15:00-16:00'),
               ('16:00-17:00', '16:00-17:00'), ('17:00-18:00', '17:00-18:00'), ('18:00-19:00', '18:00-19:00')
               ]
               
    SINIFLAR = [
        (1, '1. Sınıf'),
        (2, '2. Sınıf'),
        (3, '3. Sınıf'),
        (4, '4. Sınıf')
    ]

    ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
    derslik = models.ForeignKey(Derslik, on_delete=models.CASCADE)
    gun = models.CharField(max_length=20, choices=GUNLER)
    saat = models.CharField(max_length=20, choices=SAATLER)
    online_mi = models.BooleanField(default=False)
    sinif = models.IntegerField(choices=SINIFLAR, verbose_name='Sınıf', default=1)

    class Meta:
        verbose_name_plural = "Ders Programları"

    def __str__(self):
        return f"{self.ders.ad} - {self.gun} {self.saat}"
