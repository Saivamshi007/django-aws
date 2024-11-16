from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from .models import Profile
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'index.html')

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
            print('sai')
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')

            
            
            
    context = {'form':form}
    return render(request,'login.html',context=context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            profile = Profile.objects.create(user=current_user)

            return redirect('login')

    context = {'form':form}    
        
    return render(request,'register.html',context=context)
@login_required(login_url='login')
def profile(request):

    userform = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        userform = UpdateUserForm(request.POST,instance=request.user)

        if userform.is_valid():
            userform.save()
            return redirect('dashboard')

    context = {
        'userform':userform,

    }

    return render(request,'profile_mangement.html',context=context)

@login_required(login_url='login')
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)
    context = {'profile_pic':profile_pic}
    return render(request,'dashboard.html',context=context)

def delete_account(request):
    if request.method == 'POST':

        deleteuser = User.objects.get(username=request.user)
        deleteuser.delete()

        return redirect("")

    return render(request,'delete_account.html')

def logout(request):
    auth.logout(request)
    return redirect("")
    