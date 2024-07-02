from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'register.html')

def registerdata(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('firstname')
    lname=request.POST.get('lastname')
    email=request.POST.get('email')
    password=request.POST.get('password')
    print(name,lname,email,password)
    