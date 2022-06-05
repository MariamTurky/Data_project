from django.shortcuts import render
from django.http import HttpResponse
# from pages.models import Contact_US
from django.core.mail import send_mail
# Create your views here.

def index(request): 
    return render(request , 'pages/index.html')



# def index1(request): 
#     if request.method == "POST":
#         contact=Contact_US()
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         contact.email=email
#         contact.subject=subject
#         contact.message= message
#         contact.save()
#         # return HttpResponse("<h1>THNKS FOR CONTACT US</h1>")

#     return render(request , 'pages/index.html')

