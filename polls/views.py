from django.shortcuts import render
from django.http import HttpResponse

def wing(request):
    return render(request,"login.html")
