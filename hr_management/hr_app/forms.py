from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'department', 'hire_date', 'mentor', 'contact_details']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if Employee.objects.filter(full_name=full_name).exists():
            raise forms.ValidationError('Сотрудник с таким именем уже существует.')
        return full_name
