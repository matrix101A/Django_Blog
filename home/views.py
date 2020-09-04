from django.shortcuts import render,HttpResponse

# Create your views here

class test():
    def get(self,request):
        return (HttpResponse('HEllo World'))


def home(request):
    return render(request,'home/home.html')



def contact(request):
    return render(request,'home/contact.html')


def about(request):
    return (HttpResponse('About page'))
