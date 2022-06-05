from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Appointment, Doctor, Nurse, Patient
# Create your views here.


def signa(request):
    return render(request, 'accounts/signa.html')


def signd(request):
    return render(request, 'accounts/signd.html')

def home2 (request):
    if request.method == "POST":
        if Doctor.objects.filter(Email = request.POST['Email'],Password = request.POST['Password']).exists():
            data =Doctor.objects.get(Email = request.POST['Email'],
            Password = request.POST['Password'])
            data=Doctor.objects.all()
            appointment = Appointment.objects.all()
            return render(request, 'accounts/doctor.html', {'data': data,'appointment':appointment})
            
        else:
            context={'msg': 'Try again invalid Email or password'}
            return render(request , 'accounts/signn.html',context)
   


def signn(request):
    return render(request, 'accounts/signn.html')
def home1(request):
    if request.method == "POST":
        if Nurse.objects.filter(Email = request.POST['Email'],Password = request.POST['Password']).exists():
            data =Nurse.objects.get(Email = request.POST['Email'],
            Password = request.POST['Password'])
            data=Nurse.objects.all()
            return render(request, 'accounts/nurse.html', {'data': data})
        else:
            context={'msg': 'Try again invalid Email or password'}
            return render(request , 'accounts/signn.html',context)

def signp(request):
    return render(request, 'accounts/signp.html')


def home(request):
    if request.method == "POST":
        if Patient.objects.filter(Email = request.POST['Email'],Password = request.POST['Password']).exists():
            data =Patient.objects.get(Email = request.POST['Email'],
            Password = request.POST['Password'])
            data=Patient.objects.all()
            return render(request, 'accounts/patient.html', {'data': data})
        else:
            context={'msg': 'Try again invalid Email or password'}
            return render(request , 'accounts/signp.html',context)
    # view doctor 
def doctor(request):
    data = Doctor.objects.all()
    x={'data':data}
    return render(request , 'accounts/doctor.html',x)
    # view nurse
def nurse(request):
    data = Nurse.objects.all()
    x={'data':data}
    return render(request , 'accounts/nurse.html',x)
def patient(request):
    data = Patient.objects.all()
    x={'data':data}
    return render(request , 'accounts/patient.html',x)

def appointment(request):
    appointment = Appointment.objects.all()
    x={'appointment':appointment}
    return render(request , 'accounts/doctor.html',x)

def appointmentp(request): 
    if request.method == "POST":
        appointment = Appointment()
        name = request.POST['name']
        Mobil = request.POST['Mobil']
        Email = request.POST['Email']
        date = request.POST['date']
        upload = request.POST['upload']
        time= request.POST['time']
        appointment.name=name
        appointment.Mobil=Mobil
        appointment.Email= Email
        appointment.date=date
        appointment.upload=upload
        appointment.time= time
        appointment.save()
        # return HttpResponse("<h1>THNKS</h1>")

    return render(request , 'accounts/patient.html')




