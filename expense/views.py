from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from .models import Expense

def index(request: HttpRequest):
    expenses = Expense.objects.all()
    error = request.GET.get("error")
    return render(request, "expense/index.html", {"expenses": expenses, "error": error})


def add_expense(request: HttpRequest):
    new_expense = request.POST.get("expense")
    price = request.POST.get("price")
    try:
        price = float(price)
    except Exception:
        err_message = "price is invalid"
        target_url = f"{reverse("expense:index")}?error={err_message}"
        return redirect(target_url)

    if price <= 0:
        err_message = "price is less than or equal to zero"
        target_url = f"{reverse("expense:index")}?error={err_message}"
        return redirect(target_url)
    if new_expense.strip() == "":
        err_message = "expense is empty"
        target_url = f"{reverse("expense:index")}?error={err_message}"
        return redirect(target_url)

    new_expense = Expense(expense=new_expense, price=price)
    new_expense.save()
    return HttpResponseRedirect(reverse("expense:index"))