from django.shortcuts import render
from .models import User_info, Property_info


def home(request):
    user = User_info.objects.all()
    return render(request, 'home.html', {'u': user})

def user_info(request, id):
    user = User_info.objects.get(id=id)
    return render(request, 'user_info.html', {'u': user})

def garden(request, id):
    user = User_info.objects.get(id=id)
    return render(request, 'garden.html', {'u': user})

def kadastr(request, id, ):
    user = Property_info.objects.get(id=id)
    return render(request, 'kadastr.html', {'u': user})

