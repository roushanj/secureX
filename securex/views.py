from django.shortcuts import render
from django.http import HttpResponse


def webpage(request):
     #html = "<html><body>This is the main server site</body></html>"
     
     return render(request,"base.html")
    
