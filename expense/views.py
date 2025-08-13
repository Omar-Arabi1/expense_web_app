from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponseRedirect, QueryDict
from django.urls import reverse
from django.core.exceptions import BadRequest

from .models import Expense


def index(request: HttpRequest):
    expenses = Expense.objects.all()
    lost = request.GET.get("lost")
    return render(request, "expense/index.html", {"expenses": expenses, "lost": lost})


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


def remove_expense(request: HttpRequest, expense_id: int):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return HttpResponseRedirect(reverse("expense:index"))


def update_expense(request: HttpRequest, expense_id: int):
    expense = get_object_or_404(Expense, id=expense_id)
    data = QueryDict(request.body)

    price = data.get("price")
    new_expense = data.get("expense")
    if price == "" and new_expense == "":
        return HttpResponseRedirect(reverse("expense:index"))

    try:
        if price != "":
            price = float(price)
    except Exception:
        raise BadRequest("invalid price")

    if price != "" and price <= 0:
        raise BadRequest("price is smaller than or equal to zero")

    if new_expense != "" and new_expense.strip() == "":
        raise BadRequest("expense is empty")

    if price != "":
        expense.price = price
    if new_expense != "":
        expense.expense = new_expense
    expense.save()
    return HttpResponseRedirect(reverse("expense:index"))


def calculate(request: HttpRequest):
    expenses = get_list_or_404(Expense)
    prices = []
    for expense in expenses:
        prices.append(expense.price)
    lost = sum(prices)
    target_url = f"{reverse("expense:index")}?lost={lost}"
    return HttpResponseRedirect(target_url)
