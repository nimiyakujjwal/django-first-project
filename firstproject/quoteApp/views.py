from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayQuote(request):
    return HttpResponse("<H1 align='center'> Quote of the day </H1> <br> <H2 align='center'> \"The secret of getting ahead is getting started.\" </H2>")