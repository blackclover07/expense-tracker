from django.urls import path

from home.views import (
    home,
    transaction,
    about,
    create_transaction,
    edit_transaction,
    delete_transaction,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("transactions/", transaction, name="transactions"),
    path("transactions/create", create_transaction, name="transactions_create"),
    path(
        "transactions/edit/<int:transaction_id>/",
        edit_transaction,
        name="transactions_edit",
    ),
    path(
        "transactions/delete/<int:transaction_id>/",
        delete_transaction,
        name="transactions_delete",
    ),
]
