from django.shortcuts import render,HttpResponse
from django.views import View
from . models import Contact
from django.contrib import messages
# Create your views here

class contact(View):
    def get(self,request):
        return render(request,'home/contact.html');

    def post(self,request):
        print('post')
        name=request.POST['name'];
        email=request.POST['email'];
        phone=request.POST['phone'];
        content=request.POST['content'];
        if len(name) is 0 or len(email) is 0 or len(phone) is 0 or len(content) is 0:
            messages.error(request,"Please fill all the Fields !")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your request has been received by us . We will contact you soon ')
        return render(request,'home/contact.html');

def home(request):
    return render(request,'home/home.html')


def about(request):
    return (HttpResponse('About page'))
