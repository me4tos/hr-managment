from django.shortcuts import render

def home(request):
    return render(request, 'hr_app/home.html')

def about(request):
    return render(request, 'hr_app/about.html')
