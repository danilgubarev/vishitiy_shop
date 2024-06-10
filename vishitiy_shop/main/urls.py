from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name='index'),
    path("get_algolia_credentials/", views.get_algolia_credentials, name="get_algolia_credentials"),
]