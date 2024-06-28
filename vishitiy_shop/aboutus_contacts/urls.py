from django.urls import path
from . import views

app_name = 'aboutus_contacts'

urlpatterns = [
    # урл для отображения главной страницы
    path('about_us/', views.aboutus, name='about'),
    path('contact/', views.contacts, name='contact')
]