from django.shortcuts import render
from django.http import HttpResponse
#from .models import django_cotent_type
from .models import Azureex

# Create your views here.

def index(request):  # 어떤url요청에대해서 index가 실행되는지 조건을 설정해줘야함
    azureexs = Azureex.objects.all()
    context = {'azureexs': azureexs}
    return render(request, 'catalog/Test1.html', context)


