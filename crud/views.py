from django.shortcuts import render
from crud.models import EmpModel
from django.contrib import messages
from crud.forms import Empforms

def showemp(request):
    showall=EmpModel.objects.all().order_by('salary')
    return render(request, 'crud/index.html', {'data':showall} )

    #class META:
        #ordering = ['salary']

def insertemp(request):
    if request.method == 'POST':
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord = EmpModel()
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.occupation=request.POST.get('occupation')
            saverecord.salary=request.POST.get('salary')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request, 'Employee ' + saverecord.empname + ' saved succesfully!')
            return render(request, 'crud/insert.html')
    else:
            return render(request, 'crud/insert.html')

def editemp(request, id):
    editempobj=EmpModel.objects.get(id=id)
    return render(request, 'crud/edit.html', {"EmpModel":editempobj})

def updateemp(request, id):
    Updateemp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST, instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated successfully!')
        return render(request, 'crud/edit.html', {"EmpModel":Updateemp})

def deleteemp(request, id):
    deleteemployee=EmpModel.objects.get(id=id)
    deleteemployee.delete()
    showdata=EmpModel.objects.all()
    return render(request, 'crud/index.html', {"data": showdata})
