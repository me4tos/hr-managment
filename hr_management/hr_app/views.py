from django.shortcuts import render, redirect
from .forms import EmployeeForm

def home(request):
    return render(request, 'hr_app/home.html')

def about(request):
    return render(request, 'hr_app/about.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # После добавления перенаправить на главную
    else:
        form = EmployeeForm()
    return render(request, 'hr_app/add_employee.html', {'form': form})