from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def register(request):
    return render(request,'df_user/register.html')

