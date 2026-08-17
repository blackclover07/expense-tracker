from django.urls import path

from home.views import home, transaction, about, create_transaction

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("transactions/", transaction, name="transactions"),
    path("transactions/create", create_transaction, name="transactions_create"),
]
