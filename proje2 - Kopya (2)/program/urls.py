from django.urls import path
from .views import ders_ekle, ders_programi_excel, ders_programi_list

app_name = 'program'

urlpatterns = [
    path('ders-ekle/', ders_ekle, name='ders_ekle'),  # Yeni ders eklemek için
    path('ders-programi/', ders_programi_list, name='ders_programi_list'),  # Ders programı listesi
    path('ders-programi/excel/', ders_programi_excel, name='ders_programi_excel'),  # Excel çıktısı almak için
] 