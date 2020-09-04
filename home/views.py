from django.shortcuts import render,HttpResponse
from django.views import View
from . models import Contact
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
        contact=Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
        return render(request,'home/contact.html');

def home(request):
    return render(request,'home/home.html')


def about(request):
    return (HttpResponse('About page'))
