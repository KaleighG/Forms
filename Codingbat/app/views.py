from django.shortcuts import render
from app.forms import FontForm, TeenForm, XyzForm, AvgForm
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def font_times(request: HttpRequest) -> HttpResponse:
    form = FontForm(request.GET)
    if form.is_valid():
        word = form.cleaned_data["word"]
        num = form.cleaned_data["num"]
        front_len = 3

        if front_len > len(word):
            front_len = len(word)
        front = word[:front_len]
        
        result = ""
        for i in range(num):
            result = result + front
        return render(request, "font.html", {"form": form, "word": word, "num": num, "result": result})
    else:
        return render(request, "font.html", {"form": form})

def no_teen_sum(request: HttpRequest) -> HttpResponse:
    form = TeenForm(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]


        def fix_teen(n):
            return 0 if (n >= 13 and n <= 19) and not (n == 15 or n == 16) else n
            
        tot = fix_teen(a) + fix_teen(b) + fix_teen(c)
        return render(request, "teen.html", {"form": form, "a": a, "b": b, "c": c, "tot": tot})
    else: 
        return render(request, "teen.html", {"form": form})
def xyz_there(request: HttpRequest) -> HttpResponse:
    a = False
    form = XyzForm(request.GET)
    if form.is_valid():
        xyz = form.cleaned_data["xyz"]
        for i in range(len(xyz) - 2):
            if xyz[i:i+3] == 'xyz' and (i == 0 or xyz[i-1] != '.'):
                a = True
        return render(request, "xyz.html", {"form": form, "xyz": xyz, "a": a})
    else:
        return render(request, "xyz.html", {"form": form})

def centered_avg(request: HttpRequest) -> HttpResponse:
    form = AvgForm(request.GET)
    if form.is_valid():
        num1 = form.cleaned_data["num1"]
        num2 = form.cleaned_data["num2"]
        num3 = form.cleaned_data["num3"]
        num4 = form.cleaned_data["num4"]
        num5 = form.cleaned_data["num5"]
        num6 = form.cleaned_data["num6"]
        num7 = form.cleaned_data["num7"]

        nums = [num1, num2, num3, num4, num5, num6, num7]
        min_val = min(nums)
        max_val = max(nums)

        nums.remove(min_val)
        nums.remove(max_val)

        avg = sum(nums) // len(nums)

    
        return render(request, "avg.html", {"form": form, "num1": num1, "num2": num2, "num3": num3, "num4": num4, "num5": num5, "num6": num6, "num7": num7, "avg": avg})
    else:
        return render(request, "avg.html", {"form": form})
