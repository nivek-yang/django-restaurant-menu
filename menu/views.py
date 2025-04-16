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
        return redirect("menu:show", id=menu.id)
    else:
        menu = Menu.objects.order_by("-id")
        return render(req, "menu/index.html", {"menu": menu})

def new(req):
    return render(req, "menu/new.html")

def show(req, id):
    menu = Menu.objects.get(pk=id)
    return render(req, "menu/show.html", {"menu": menu})

def update(req, id):
    if req.POST:
        menu = Menu.objects.get(pk=id)
        menu.name = req.POST['name']
        menu.price = req.POST['price']
        menu.description = req.POST['description']
        menu.is_available = req.POST['is_available']
        menu.is_spicy = req.POST['is_spicy']

        menu.save()
        
        return redirect("menu:show", menu.id)
        
    else:
        menu = Menu.objects.get(pk=id)
        return render(req, "menu/update.html", {"menu": menu})

def delete(req, id):
    menu = Menu.objects.get(pk=id)
    menu.delete()

    return redirect("menu:index")