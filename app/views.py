from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from .models import Smartphone
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

def smartphone_lookup(request: HttpRequest):
    data = Smartphone.objects.filter(name__icontains="Apple")
    print(len(data))
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)