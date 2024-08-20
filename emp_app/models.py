from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    reporting_manager = models.CharField(max_length=100, blank=True, null=True)  
    
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()


    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Leave(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)

class PayrollRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    request_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.subject} - {self.employee.name}"

class Report(models.Model):
    name = models.CharField(max_length=255)
    preferred_contact = models.CharField(max_length=50)
    contact_details = models.CharField(max_length=255)
    incident_date = models.DateField()
    incident_time = models.TimeField(null=True, blank=True)
    incident_description = models.TextField()
    harasser_name = models.CharField(max_length=255)
    harasser_role = models.CharField(max_length=255, blank=True)
    harasser_department = models.CharField(max_length=255, blank=True)
    witness_name = models.CharField(max_length=255, blank=True)
    evidence = models.FileField(upload_to='evidence/', blank=True)

    def __str__(self):
        return self.name
    
class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('adhar_card', 'Aadhaar Card'),
        ('graduate_certificate', 'Graduate Certificate'),
        ('experience_letter', 'Experience Letter'),
        ('passport_photo', 'Passport Size Photo'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES, default='General')
    document_file = models.FileField(upload_to='documents/', default='default_files/placeholder.pdf')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.user.username}"
    
from django.db import models

class HR_Department(models.Model):
    name = models.CharField(max_length=100)


    
class HR_Payroll(models.Model):
    employee_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models
from django.utils import timezone

class LeaveType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]

    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    date_applied = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.employee.name} - {self.start_date} to {self.end_date}"