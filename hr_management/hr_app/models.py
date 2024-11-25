from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    requirements = models.TextField()
    responsibilities = models.TextField()
    salary_level = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])

class Candidate(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    residence = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    qualifications = models.TextField()
    experience = models.TextField()
    status = models.CharField(max_length=20, choices=[('rejected', 'Rejected'), ('invited', 'Invited'), ('hired', 'Hired')])

class Interview(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    date = models.DateTimeField()
    interviewer = models.CharField(max_length=100)
    evaluation = models.TextField()
    conclusion = models.TextField()
from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Полное имя")
    position = models.CharField(max_length=100, verbose_name="Должность")
    department = models.CharField(max_length=100, verbose_name="Отдел")
    hire_date = models.DateField(verbose_name="Дата приема на работу")
    mentor = models.CharField(max_length=100, verbose_name="Наставник")
    contact_details = models.CharField(max_length=100, verbose_name="Контактные данные")

    def __str__(self):
        return self.full_name

class AdaptationProgram(models.Model):
    name = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    duration = models.IntegerField()  # in days
    employees = models.ManyToManyField(Employee, through='EmployeeAdaptation')

class EmployeeAdaptation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    adaptation_program = models.ForeignKey(AdaptationProgram, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('completed', 'Completed')])
    completion_date = models.DateField(null=True, blank=True)
class EmployeeEvaluation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    period = models.CharField(max_length=50)
    competencies = models.TextField()
    results = models.TextField()
    overall_score = models.DecimalField(max_digits=5, decimal_places=2)
    recommendations = models.TextField()

class TrainingPlan(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    organizer = models.CharField(max_length=100)
    participants = models.ManyToManyField(Employee)
    outcome = models.TextField(null=True, blank=True)
class Reward(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reward_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class MotivationProgram(models.Model):
    name = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    participants = models.ManyToManyField(Employee)
    effectiveness = models.TextField(null=True, blank=True)
class Termination(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100, choices=[('voluntary', 'Voluntary'), ('involuntary', 'Involuntary')])
    termination_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('completed', 'Completed')])
    final_report = models.TextField()

class ExitInterview(models.Model):
    termination = models.ForeignKey(Termination, on_delete=models.CASCADE)
    feedback = models.TextField()
    recommendations = models.TextField()

from django.contrib.auth.models import User

class Role(models.Model):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('hr_manager', 'HR Manager'),
        ('supervisor', 'Supervisor'),
        ('admin', 'Administrator'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
