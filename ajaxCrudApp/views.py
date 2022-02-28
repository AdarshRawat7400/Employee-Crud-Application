
from django.http import JsonResponse, request
from django.shortcuts import render
from .forms import EmployeeRegistration
from .models import Employee
from django import views
from django.http import JsonResponse
# from django.core import serializers
from django.core.paginator import Paginator
from .serializers import EmployeeSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers
import json
from django.shortcuts import redirect




class DataTableView(views.View):

    def get(self,request,pk=None):
        employees = Employee.objects.all().order_by('-id')
        form = EmployeeRegistration()


        return render(request, template_name='ajaxCrudApp/datatable_static.html', context={'employees': employees,
                                                                                            'form': form})  

@method_decorator(csrf_exempt, name='dispatch')
class CreateView(views.View):
    def post(self, request,pk=None):
        form = EmployeeRegistration(request.POST)
        
        if form.is_valid():
            print("IT IS VALID")
            emp_id = request.POST['employee_id']
            name = request.POST['employee_name']
            email = request.POST['employee_email']
            location = request.POST['employee_location']
            phone = request.POST['employee_phone']
            print(f"ID {emp_id}")
            if(emp_id == ""):
                employee = Employee.objects.create(employee_name=name,
                                        employee_email=email, 
                                        employee_location=location,
                                        employee_phone=phone)
            else:
                print("IT IS NOT VALID")
                employee = Employee(
                                        id = emp_id,
                                        employee_name=name,
                                        employee_email=email, 
                                        employee_location=location,
                                        employee_phone=phone)
            employee.save()
           
           
            serializer = EmployeeSerializer(employee)
            employees = Employee.objects.values().order_by('-id')
            employees_list = list(employees)
            
            return JsonResponse({'status': 1,'employees_data': serializer.data, 'employees': employees_list})
        else:
            return JsonResponse({'status': 0})

class DeleteView(views.View):
    def post(self, request,pk=None):
        id = request.POST['sid']
        # print(id)
        employee = Employee.objects.get(pk=id)
        employee.delete()
        
        employees_data = list(Employee.objects.values())
        return JsonResponse({'status': 1})

class UpdateView(views.View):
    def post(self, request,pk=None):
        id = request.POST['sid']
        print(id)
        employee = Employee.objects.get(pk=id)
        employee_data = {
            "id": employee.id,
            "employee_name": employee.employee_name,
            "employee_email": employee.employee_email,
            "employee_location": employee.employee_location,
            "employee_phone": employee.employee_phone

        }
        return JsonResponse(employee_data)
        


 




    
  