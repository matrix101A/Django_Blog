from django.shortcuts import render,HttpResponse

# Create your views here

class test():
    def get(self,request):
        return (HttpResponse('HEllo World'))


def blogHome(request):
    return (HttpResponse('All blog posts here'))

def blogPost(request,slug):
    return HttpResponse(f'All blog posts here{slug}')
