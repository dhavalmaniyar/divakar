from django.shortcuts import render
from .models import *;
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def comment_submit(request):
    rname=request.POST['name']
    rcomment=request.POST['comment']
    remail=request.POST['email']
    submitData=Comment(name=rname,comment=rcomment,email=remail)
    submitData.save()
    return render(request,'index.html',{'message':'Thank you'})