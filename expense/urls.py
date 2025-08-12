from django.urls import path

from . import views

app_name = "expense"
urlpatterns = [
    path("", views.index, name='index'),
    path('add_expense', views.add_expense, name="add_expense"),
]