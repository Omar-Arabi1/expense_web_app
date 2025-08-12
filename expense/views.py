from django.shortcuts import render
from django.http import HttpRequest

from .models import Expense

def index(request: HttpRequest):
    expenses = Expense.objects.all()
    error = request.GET.get("error")
    return render(request, "expense/index.html", {"expenses": expenses, "error": error})
