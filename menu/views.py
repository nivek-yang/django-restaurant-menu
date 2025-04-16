from django.shortcuts import render, redirect
from .models import Menu

# Create your views here.
def index(req):
    if req.method == "POST":
        menu = Menu.objects.create(
            name=req.POST['name'],
            price=req.POST['price'],
            description=req.POST['description'],
            is_available=req.POST['is_available'] == 'True',
            is_spicy=req.POST['is_spicy'] == 'True',
        )
        return redirect("menu:index")
    else:
        return render(req, "menu/index.html")

def new(req):
    return render(req, "menu/new.html")
    