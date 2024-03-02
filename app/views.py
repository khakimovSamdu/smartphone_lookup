from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from .models import Smartphone
from datetime import date
from practikum.main import get_random_date
# Create your views here.

def get_add(request: HttpRequest):
    if request.method=='POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        ram = ''
        rom = ''
        for i in data['RAM']:
            if i.isdigit():
                ram += i
            else:
                break
        for i in data['memory']:
            if i.isdigit():
                rom += i
            else:
                break
        create = Smartphone.objects.create(
            name = data['name'],
            company = data['company'],
            color = data['color'],
            RAM = int(ram),
            memory = int(rom),
            price = data['price'], 
            img_url = data['img_url'], 
            release_date = get_random_date(2000, 2024)
        )
        return JsonResponse({"statust":"OK"})
    else:
        return JsonResponse({"Method":"Error"})

def get_all(request: HttpRequest):
    data = Smartphone.objects.all()
    print(len(data))
    ruyxat = []
    for item in data:
        ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_id(request: HttpRequest, id: int):
    try:
        data = Smartphone.objects.get(id=id)
        return JsonResponse(data.to_dict(), safe=False)
    except:
        return HttpResponse("Server error or id error")

def brend_item_delete(request: HttpRequest, id: int):
    try:
        data = Smartphone.objects.filter(id=id).delete()
        data = Smartphone.objects.all()
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return HttpResponse("Server error or id error")
    
def brend_item_update(request: HttpRequest, id: int):
    try:
        data = Smartphone.objects.filter(id=id)
        data.update(
            name = "Infinix Hot 11 Play"
        )
        data = Smartphone.objects.all()
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return HttpResponse("Server error or id error")

def smartphone_orderby(request: HttpRequest):
    data = Smartphone.objects.order_by('-release_date')
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def smartphone_filter(request: HttpRequest):
    data = Smartphone.objects.filter(memory=128)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_brend_name(request: HttpRequest):
    data = Smartphone.objects.all()
    ruyxat = []
    for item in data:
        print(item)
        ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def brend_all(request: HttpRequest, brend: str):
    data = Smartphone.objects.filter(company__contains=brend)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)


def smartphone_lookup(request: HttpRequest):
    data = Smartphone.objects.filter(name__icontains="Apple")
    print(len(data))
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def contains(request:HttpRequest):
    # Case-sensitive containment test. uzb Kata-kichik harflar sezgirligi testi
    inner_qs = Smartphone.objects.filter(name__contains = "apple").values("name")
    data = Smartphone.objects.filter(name__contains = "vivo")
    print(len(data))
    ruyxat = []
    for item in inner_qs:
            ruyxat.append(item)
    return JsonResponse(ruyxat, safe=False)

def icontains(request: HttpRequest):
    #Case-insensitive containment test. uzb Katta - kichik harflarni sezmaydigan testi
    data = Smartphone.objects.filter(color__icontains = 'gold')
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def data_in(request: HttpRequest):
    inner_qs = Smartphone.objects.filter(name__contains='apple')
    data = Smartphone.objects.filter(RAM__in = [2,4,6])
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def gt(request: HttpRequest, n: int):
    data = Smartphone.objects.filter(memory__gt=n)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def gte(request: HttpRequest, n: int):
    data = Smartphone.objects.filter(id__gte=n)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def lt(request: HttpRequest, n: int):
    data = Smartphone.objects.filter(memory__lt=n)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def lte(request: HttpRequest, n: int):
    data = Smartphone.objects.filter(id__lte=n, id__gte=1)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def startswith(request: HttpRequest):
    data = Smartphone.objects.filter(id__startswith=2)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def endswith(request: HttpRequest):
    data = Smartphone.objects.filter(id__endswith= 1)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def data_range(request: HttpRequest):
    start_date = date(2016, 1, 1)
    end_date = date(2024, 1, 1)
    data = Smartphone.objects.filter(release_date__range=(start_date, end_date))
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_year(request: HttpRequest, year: int):
    data = Smartphone.objects.filter(release_date__year__gte=year)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_month(request: HttpRequest, month: int):
    data = Smartphone.objects.filter(release_date__month__lte=month)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)
    
def get_day(request: HttpRequest, day: int):
    data = Smartphone.objects.filter(release_date__day=day)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_week(request: HttpRequest, week: int):
    data = Smartphone.objects.filter(release_date__week__gte=1, release_date__week__lte=week)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_week_day(request: HttpRequest, week_day: int):
    data = Smartphone.objects.filter(release_date__week_day = week_day)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_quarter(request: HttpRequest, n: int):
    #Yil choragini ifodalovchi 1 dan 4 gacha bo'lgan butun qiymatni oladi.
    data = Smartphone.objects.filter(release_date__quarter = n)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def bool_isnull(request: HttpRequest):
    data = Smartphone.objects.filter(name__isnull=False)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_regex(request: HttpRequest, s: str):
    # Katta-kichik harflarga sezgir muntazam ifoda mosligi.
    
    data = Smartphone.objects.filter(color__regex = s)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)