from django.shortcuts import render
from . models import Book

# Create your views here.

def purple(request):
    return render(request,"web/purple.html")

def chart(request):
    return render(request,"web/pages/charts/chartjs.html")

def forms(request):
    return render(request,"web/pages/forms/basic_elements.html")

def icons(request):
    return render(request,"web/pages/icons/mdi.html")

def register(request):
    return render(request,"web/pages/samples/register.html")

def login(request):
    return render(request,"web/pages/samples/login.html")

def tables(request):
    return render(request,"web/pages/tables/basic-table.html")

def buttons(request):
    return render(request,"web/pages/ui-features/buttons.html")

def typography(request):
    return render(request,"web/pages/ui-features/typography.html")