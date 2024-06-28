from django.urls import path
from . import views


app_name = "payments"

urlpatterns = [
    path("", views.email_form, name="email"),
    path("get-post-offices/", views.get_post_offices_view, name="get-post-offices"),
    path("webhook/", views.monobank_webhook_view, name="webhook"),
    path("payment-status/", views.payment_status_view, name="payment-status"),
    path("monobank-payment/", views.monobank_form_view, name="monobank-payment"),
]