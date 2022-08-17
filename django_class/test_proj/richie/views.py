from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    
    return HttpResponse("<h1>This is our home page</h1>")
    
def another_page(request):
    return HttpResponse("<h1>Another page</h1>")


def login_page(request):
    return render(request, "signup.html")