from django.shortcuts import render

# Create your views here.

def firstTemplateView(request):
    return render(request, 'templatesApp/firstTemplate.html')
