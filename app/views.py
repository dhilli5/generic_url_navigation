from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request,'hi.html')


def hello(request):
    return render(request,'hello.html')