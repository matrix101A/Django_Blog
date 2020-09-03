from django.shortcuts import render,HttpResponse

# Create your views here

class test():
    def get(self,request):
        return (HttpResponse('HEllo World'))


def home(request):
    return (HttpResponse('HEllo World'))



def contact(request):
    return (HttpResponse('Contact page'))


def about(request):
    return (HttpResponse('About page'))
