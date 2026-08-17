from django.contrib import admin
from transaction.models import Transaction


# Register your models here.


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Transaction._meta.fields if field.name != "description"
    ]
    list_filter = (
        "user",
        "transaction_type",
        "date",
    )
