from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def longBoat(request):
    return HttpResponse('in this we have a good drinks')
def loot(request):
    return HttpResponse('looting is very dangerous')