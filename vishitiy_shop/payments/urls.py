from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("", views.email_form, name="email"),
    path("get-post-offices/", views.get_post_offices_view, name="get-post-offices"),
]
