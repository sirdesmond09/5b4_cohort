from django.urls import path
from . import views

urlpatterns = [
    path('richie/', views.home_page),
    path("somnvsf/", views.another_page),
    path("signup/", views.login_page)
]
