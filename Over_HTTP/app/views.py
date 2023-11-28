from django.shortcuts import render
from app.forms import HelloForm, AgeForm, OrderForm
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def hey_name(request: HttpRequest) -> HttpResponse:
    form = HelloForm(request.GET)
    if form.is_valid(): 
        user_name = form.cleaned_data["user_name"]
        return render(request, "index.html", {"form": form, "user_name": user_name})
    else:
        return render(request, "index.html", {"form": form})    
    
def how_old(request: HttpRequest) -> HttpResponse:
    form = AgeForm(request.GET)

    if form.is_valid():
        end = form.cleaned_data["endyear"]
        birth_year = form.cleaned_data["birthyear"]
        age = end - birth_year
        return render(request, "age.html", {"birth_year": birth_year, "end": end, "age": age, "form": form})
    else: 
        return render(request, "age.html", {"form": form})
    
def order(request: HttpRequest) -> HttpResponse: 
    form = OrderForm(request.GET)
    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = (burgers * 4.5) + (fries * 1.5) + (drinks * 1)
        return render(request, "order.html", {"burgers": burgers, "fries": fries, "drinks": drinks, "total": total, "form": form})
    else:
        return render(request, "order.html", {"form": form})

    
