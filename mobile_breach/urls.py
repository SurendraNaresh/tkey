from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("breach_reports/", views.BreachReport, name="breach_reports"),
    path("breach_add/", views.breach_add, name="breach_add"),
    path("breach_list/", views.breach_list, name="breach_list"),
]
