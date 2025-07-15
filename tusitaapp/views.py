from django.shortcuts import render 
from django.http import HttpResponse 

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def gallery(request):
    return render(request,"gallery.html")

def AS(request):
    return render(request,"AS.html")

def inA(request):
    data = [
        {'name': 'สมชาย', 'age': 25, 'date': '01/07/2025'},
        {'name': 'สมหญิง', 'age': 28, 'date': '02/07/2025'},
        {'name': 'นารี', 'age': 22, 'date': '02/07/2025'},
    ]
    return render(request, 'inA.html', {'data': data})