from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Inquiry;
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def contact(request):
    return render(request,'contact.html')

def submit(request):
    name=request.POST['name']
    mobile=request.POST['mobile']
    email=request.POST['email']
    inquiry=request.POST['inquiry']
    # pay=request.POST['pay']
    # need=request.POST['need']
    data=Inquiry(name=name,mobile=mobile,email=email,inquiry=inquiry)
    data.save()
    subject = 'Free Consultation Inquiry'
    # emailmessage = 'name: '+name+'\nmobile: '+mobile+'\nemail: '+email+'\nInquiry: '+inquiry+'\nRequirements: '+need
    messages.success(request,'Thank You, we will contact you soon')
    # render(request,'consulting.html',{'message':"Thank You, we will contact you soon"})
    return redirect('consulting')