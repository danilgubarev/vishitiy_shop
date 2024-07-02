from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path("", views.email_form, name="email"),
    path("get-post-offices/", views.get_post_offices_view, name="get-post-offices"),
    path("monobank-webhook/", views.monobank_webhook, name="monobank-webhook"),
    path("payment-status/", views.payment_status_view, name="payment-status"),
    path("pay-with-card/", views.payment_view, name="pay-with-card"),
]
