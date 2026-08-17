from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("INCOME", "Income"),
        ("EXPENSE", "Expense"),
    ]

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    category = models.CharField(max_length=50)

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
    )

    description = models.TextField()

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
