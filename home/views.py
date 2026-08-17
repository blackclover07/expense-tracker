from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect, render

from transaction.forms import TransactionForm
from transaction.models import Transaction

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@login_required
def transaction(request):
    user_transactions = Transaction.objects.filter(user=request.user).order_by(
        "-date", "-created_at"
    )

    total_income = (
        user_transactions.filter(transaction_type="INCOME").aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )

    total_expense = (
        user_transactions.filter(transaction_type="EXPENSE").aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )

    balance = total_income - total_expense

    return render(
        request,
        "transaction.html",
        {
            "transactions": user_transactions,
            "total_income": total_income,
            "total_expenses": total_expense,
            "balance": balance,
        },
    )


@login_required
def create_transaction(request):

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)

            transaction.user = request.user

            transaction.save()
            messages.success(request, "transaction created sucessfully")
            return redirect(request.path)
    else:
        form = TransactionForm()
    return render(request, "transaction-form.html", {"form": form})
