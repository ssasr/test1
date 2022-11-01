from django.shortcuts import render
from .forms import signup_Form
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def base_view(request):
    return render(request,'testapp/base.html')
@login_required
def python_view(request):
    return render(request,'testapp/python.html')

@login_required
def java_view(request):
    return render(request,'testapp/java.html')

def signup_model_view(request):
    frm=signup_Form()
    if request.method=="POST":
        frm=signup_Form(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{"FORM":frm})

def logout_view(request):
    return render(request,'testapp/logout.html')
