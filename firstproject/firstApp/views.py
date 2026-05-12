from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def display(request):
    return HttpResponse("<H1>Hello Django Developer</H1>")

def displayDateTime(request):
    now = datetime.now()
    return HttpResponse("<H1>Current date time is: </H1>" + str(now))