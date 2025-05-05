from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from .models import Ders, DersProgrami, Derslik, Bolum, Kullanici
from .views import ders_programi_excel

class DersProgramiAdmin(admin.ModelAdmin):
    list_display = ('get_bolum', 'get_ders_kodu', 'get_ders_adi', 'sinif', 'gun', 'saat', 'get_derslik', 'online_mi')
    list_filter = ('sinif', 'gun', 'ders__bolum', 'online_mi')
    search_fields = ('ders__ad', 'ders__kod')
    ordering = ('sinif', 'gun', 'saat')
    actions = ['download_excel']
    
    def get_bolum(self, obj):
        return obj.ders.bolum.ad
    get_bolum.short_description = 'Bölüm'
    get_bolum.admin_order_field = 'ders__bolum__ad'
    
    def get_ders_kodu(self, obj):
        return obj.ders.kod
    get_ders_kodu.short_description = 'Ders Kodu'
    get_ders_kodu.admin_order_field = 'ders__kod'
    
    def get_ders_adi(self, obj):
        return obj.ders.ad
    get_ders_adi.short_description = 'Ders Adı'
    get_ders_adi.admin_order_field = 'ders__ad'
    
    def get_derslik(self, obj):
        return f"Derslik {obj.derslik.id}"
    get_derslik.short_description = 'Derslik'
    
    def download_excel(self, request, queryset):
        return ders_programi_excel(request)
    download_excel.short_description = "Seçili dersleri Excel olarak indir"

class DersAdmin(admin.ModelAdmin):
    list_display = ('kod', 'ad', 'bolum', 'haftalik_saat', 'ogretim_uyesi')
    list_filter = ('bolum',)
    search_fields = ('ad', 'kod')
    ordering = ('kod',)

class DerslikAdmin(admin.ModelAdmin):
    list_display = ('ad', 'kapasite', 'statu')
    list_filter = ('statu',)
    ordering = ('ad',)

class BolumAdmin(admin.ModelAdmin):
    list_display = ('kod', 'ad')
    search_fields = ('ad', 'kod')
    ordering = ('kod',)

class KullaniciAdmin(admin.ModelAdmin):
    list_display = ('isim', 'soyisim', 'email', 'rol')
    list_filter = ('rol',)
    search_fields = ('isim', 'soyisim', 'email')
    ordering = ('isim', 'soyisim')

admin.site.register(DersProgrami, DersProgramiAdmin)
admin.site.register(Ders, DersAdmin)
admin.site.register(Derslik, DerslikAdmin)
admin.site.register(Bolum, BolumAdmin)
admin.site.register(Kullanici, KullaniciAdmin)

# Admin site başlığını ve başlık çubuğunu özelleştir
admin.site.site_header = 'Ders Programı Yönetim Sistemi'
admin.site.site_title = 'Ders Programı Yönetimi'
admin.site.index_title = 'Yönetim Paneli'
