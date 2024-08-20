from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.shortcuts import render, get_object_or_404
from .forms import EmployeeForm
from django.core.mail import send_mail
from django.contrib import messages
from .forms import InternalMessageForm
from .models import Profile, Leave, HR_Payroll
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Document
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
from .models import Employee, PayrollRequest




# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new employee record to the database
            return redirect('all_emp')  # Redirect to a page listing employees or a success page
    else:
        form = EmployeeForm()
    return render(request, 'add_emp.html', {'form': form})

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')



def finance_employees(request):
    # Assuming "Finance" is a unique department name
    try:
        finance_department = Department.objects.get(name='Finance')
    except Department.DoesNotExist:
        finance_department = None
    
    if finance_department:
        employees = Employee.objects.filter(dept=finance_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'finance_employees.html', {'emps': employees})

def sales_employees(request):
    # Assuming "Sales" is a unique department name
    try:
        sales_department = Department.objects.get(name='Sales')
    except Department.DoesNotExist:
        sales_department = None
    
    if sales_department:
        employees = Employee.objects.filter(dept=sales_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'sales_employees.html', {'emps': employees})

def digital_employees(request):
    # Assuming "Digital" is a unique department name
    try:
        digital_department = Department.objects.get(name='Digital')
    except Department.DoesNotExist:
        digital_department = None
    
    if digital_department:
        employees = Employee.objects.filter(dept=digital_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'digital_employees.html', {'emps': employees})

def management(request):
    # Assuming "Directors" is a unique department name
    try:
        management_department = Department.objects.get(name='Management')
    except Department.DoesNotExist:
        management_department = None
    
    if management_department:
        employees = Employee.objects.filter(dept=management_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'management.html', {'emps': employees})

def hr_employees(request):
    # Assuming "HR" is a unique department name
    try:
        hr_department = Department.objects.get(name='Human Resource')
    except Department.DoesNotExist:
        hr_department = None
    
    if hr_department:
        employees = Employee.objects.filter(dept=hr_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'hr_employees.html', {'emps': employees})

def it_employees(request):
    # Assuming "Digital" is a unique department name
    try:
        it_department = Department.objects.get(name='Information Technology')
    except Department.DoesNotExist:
        it_department = None
    
    if it_department:
        employees = Employee.objects.filter(dept=it_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'it_employees.html', {'emps': employees})


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def edit_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('all_emp')  # Redirect to a list view or wherever you need
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

def landing_page(request):
    return render(request, 'landing_page.html')



def employee_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('employee_home')
    else:
        form = LoginForm()
    return render(request, 'employee_login.html', {'form': form})

def hr_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('hr_home')
    else:
        form = LoginForm()
    return render(request, 'hr_login.html', {'form': form})



def internal_message(request):
    if request.method == 'POST':
        form = InternalMessageForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            cc = form.cleaned_data['cc']
            subject = form.cleaned_data['subject']
            reason = form.cleaned_data['reason']
            
            # Sending email logic (customize as needed)
            send_mail(
                subject,
                reason,
                email_address,
                [email_address] + [cc] if cc else [],
                fail_silently=False,
            )
            messages.success(request, 'Internal message sent successfully.')
            return redirect('index')  # Redirect to admin home or another page
    else:
        form = InternalMessageForm()

    return render(request, 'internal_message.html', {'form': form})

def employee_home(request):
    return render(request, 'employee_home.html')




def my_profile(request):
    emps = Employee.objects.all()  # Fetch employee details
    context = {
        'emps': emps
    }
    return render(request, 'my_profile.html', context)


def leave_manager(request):
    leaves = Leave.objects.filter(employee=request.user)
    return render(request, 'leave_manager.html', {'leaves': leaves})


def payroll(request):
    payrolls = HR_Payroll.objects.filter(employee=request.user)
    return render(request, 'payroll.html')


def posh(request):
    # Implement Posh related functionality here
    return render(request, 'posh.html')



from django.contrib.auth.models import User
from emp_app.models import Profile

from django.contrib.auth.models import User
from emp_app.models import Profile

# Create profile for existing users if they don't have one
for user in User.objects.all():
    if not Profile.objects.filter(user=user).exists():
        Profile.objects.create(user=user)

from .models import Leave

@login_required
def leave_manager(request):
    return render(request, 'leave_manager.html')

@login_required
def leave_balance(request):
    # Fetch leave balance from the database
    # Example: leave_balance = get_leave_balance(request.user)
    return render(request, 'leave_balance.html')

@login_required
def apply_leave(request):
    if request.method == 'POST':
        # Handle leave application form submission
        pass
    return render(request, 'apply_leave.html')

@login_required
def leave_status(request):
    leaves = Leave.objects.filter(employee=request.user)
    return render(request, 'leave_status.html', {'leaves': leaves})

@login_required
def leave_history(request):
    leaves = Leave.objects.filter(employee=request.user).order_by('-start_date')
    return render(request, 'leave_history.html', {'leaves': leaves})

@login_required
def leave_calendar(request):
    # Implement calendar functionality if required
    return render(request, '/leave_calendar.html')

def report_now(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        preferred_contact = request.POST.get('preferred_contact')
        contact_details = request.POST.get('contact_details')
        incident_date = request.POST.get('incident_date')
        incident_time = request.POST.get('incident_time')
        incident_description = request.POST.get('incident_description')
        harasser_name = request.POST.get('harasser_name')
        harasser_role = request.POST.get('harasser_role')
        harasser_department = request.POST.get('harasser_department')
        witness_name = request.POST.get('witness_name')
        evidence = request.FILES.get('evidence')
        
        # Handle the evidence file
        if evidence:
            file_name = default_storage.save(evidence.name, ContentFile(evidence.read()))
        
        # Save the report details (you might want to save these to a database)
        # For example: Report.objects.create(...)
        
        return redirect('posh')
    
    return render(request, 'posh.html')

def documents(request):
    if request.method == 'POST' and request.FILES:
        # Handle file uploads
        uploaded_files = {
            'adhar_card': request.FILES.get('adhar_card'),
            'graduation_certificate': request.FILES.get('graduation_certificate'),
            'experience_letter': request.FILES.get('experience_letter'),
            'passport_photo': request.FILES.get('passport_photo'),
        }

        for key, file in uploaded_files.items():
            if file:
                # Save file and record details
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                file_url = fs.url(filename)
                Document.objects.create(
                    name=file.name,
                    uploaded_at=timezone.now(),
                    location=file_url,
                )

        return redirect('documents')

    files = Document.objects.all()
    return render(request, 'documents.html', {'files': files})

def reach_us(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        # Send email (use your actual email configurations)
        send_mail(
            subject,
            description,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        return redirect('employee_home')  # Redirect to home page or a thank you page

    return render(request, 'reach_us.html')

def department_employees(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    employees = department.employees.all()
    return render(request, 'department_employees.html', {'department': department, 'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})

from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    # Log out the user
    logout(request)
    # Redirect to the login page or any other page after logout
    return redirect('login')



def hr_home(request):
    return render(request, 'hr_home.html')

def hr_department(request):
    return render(request, 'hr_department.html')



def hr_payroll(request):
    return render(request, 'hr_payroll.html')

def hr_posh(request):
    return render(request, 'hr_posh.html')

def hr_internal_message(request):
    return render(request, 'hr_internal_message.html')

def hr_finance_employees(request):
    # Assuming "Finance" is a unique department name
    try:
        hr_finance_department = Department.objects.get(name='Finance')
    except Department.DoesNotExist:
        hr_finance_department = None
    
    if hr_finance_department:
        employees = Employee.objects.filter(dept=hr_finance_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'hr_finance_employees.html', {'emps': employees})

def hr_sales_employees(request):
    # Assuming "Sales" is a unique department name
    try:
        hr_sales_department = Department.objects.get(name='Sales')
    except Department.DoesNotExist:
        hr_sales_department = None
    
    if hr_sales_department:
        employees = Employee.objects.filter(dept=hr_sales_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'hr_sales_employees.html', {'emps': employees})

def hr_digital_employees(request):
    # Assuming "Digital" is a unique department name
    try:
        hr_digital_department = Department.objects.get(name='Digital')
    except Department.DoesNotExist:
        hr_digital_department = None
    
    if hr_digital_department:
        employees = Employee.objects.filter(dept=hr_digital_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'hr_digital_employees.html', {'emps': employees})

def hr_management(request):
    # Assuming "Directors" is a unique department name
    try:
        hr_management_department = Department.objects.get(name='Management')
    except Department.DoesNotExist:
        hr_management_department = None
    
    if hr_management_department:
        employees = Employee.objects.filter(dept=hr_management_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'hr_management.html', {'emps': employees})

def hr_hr_employees(request):
    # Assuming "HR" is a unique department name
    try:
        hr_hr_department = Department.objects.get(name='Human Resource')
    except Department.DoesNotExist:
        hr_hr_department = None
    
    if hr_hr_department:
        employees = Employee.objects.filter(dept=hr_hr_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'hr_hr_employees.html', {'emps': employees})

def hr_it_employees(request):
    # Assuming "Digital" is a unique department name
    try:
        hr_it_department = Department.objects.get(name='Information Technology')
    except Department.DoesNotExist:
        hr_it_department = None
    
    if hr_it_department:
        employees = Employee.objects.filter(dept=hr_it_department)
    else:
        employees = Employee.objects.none()  # Or handle the case as needed

    return render(request, 'hr_it_employees.html', {'emps': employees})


def payroll(request):
    employees = Employee.objects.all()
    return render(request, 'payroll.html', {'employees': employees})

def employee_payroll(request):
    employees = Employee.objects.all()
    return render(request, 'employee_payroll.html', {'employees': employees})

def employee_request(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        subject = request.POST.get('subject')
        employee = get_object_or_404(Employee, employee_id=employee_id)
        PayrollRequest.objects.create(employee=employee, subject=subject)
    employees = Employee.objects.all()
    return render(request, 'employee_request.html', {'employees': employees})

def view_generate(request):
    requests = PayrollRequest.objects.all()
    return render(request, 'view_generate.html', {'requests': requests})

def pay_slip(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    # Generate pay slip logic here
    context = {'employee': employee}
    return render(request, 'pay_slip.html', context)

from django.shortcuts import render
from .models import LeaveRequest  # Import your LeaveRequest model



from django.shortcuts import render
from .models import LeaveRequest

def hr_leave_manager(request):
    # Query to get all pending leave requests
    pending_requests = LeaveRequest.objects.filter(status='Pending')  # Adjust the filter based on your model's status field

    # Context to pass to the template
    context = {
        'pending_requests': pending_requests,
    }

    # Render the template with the context
    return render(request, 'hr_leave_manager.html', context)

def pending_requests(request):
    pending_requests = LeaveRequest.objects.filter(status='P')
    return render(request, 'pending_requests.html', {'pending_requests': pending_requests})

def history(request):
    history = LeaveRequest.objects.all()
    return render(request, 'history.html', {'history': history})

def calendar(request):
    calendar = LeaveRequest.objects.all()
    return render(request, 'calendar.html', {'calendar': calendar})

def swap(request):
    return render(request, 'swap.html')
