from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def send_email(request):
    time.sleep(3)
    return HttpResponse('<h1>Done sendings</h1>')