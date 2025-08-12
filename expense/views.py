from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import BadRequest

from .models import Expense


def index(request: HttpRequest):
    expenses = Expense.objects.all()
    return render(request, "expense/index.html", {"expenses": expenses})


def add_expense(request: HttpRequest):
    new_expense = request.POST.get("expense")
    price = request.POST.get("price")
    if price is None or new_expense is None:
        raise BadRequest("did not get expected fields")

    try:
        price = float(price)
    except Exception:
        raise BadRequest("invalid price")

    if price <= 0:
        raise BadRequest("price is less than or equal to zero")
    if new_expense.strip() == "":
        raise BadRequest("expense is empty")
    new_expense = Expense(expense=new_expense, price=price)
    new_expense.save()
    return HttpResponseRedirect(reverse("expense:index"))
