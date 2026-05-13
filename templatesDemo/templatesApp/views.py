from django.shortcuts import render

# Create your views here.

def firstTemplateView(request):
    return render(request, 'templatesApp/firstTemplate.html')

def employeeDetailsView(request):
    employee = {
        'name': 'John Doe',
        'age': 30,
        'department': 'Sales',
        'position': 'Manager',
    }
    return render(request, 'templatesApp/employeeTemplate.html', context={'employee': employee})
