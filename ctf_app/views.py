from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Member ,LevelsPassed
from .forms import MemberForm ,Level2Form , Level1Form , Level3Form , Level4Form , Login_Member,Level5Form,Level7Form,Level6Form,Login_Member_level3
from django.contrib.auth.decorators import login_required

from users.models import Profile

from django.contrib import messages


def home_view(request):
    level_progress = {}

    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            level_progress = user_profile.level_progress
        except Profile.DoesNotExist:
            pass
    

    if request.method == 'POST' and request.user.is_authenticated:
        
        
        form_1 = Level1Form(request.POST or None)
        if form_1.is_valid():
            if  request.POST['level1'] == "ctf-vq14e54213dds##bdsa68":   
                user_profile.pass_level('level1')
                return render(request,'home.html',{'level_progress':level_progress})
            
        form_2 = Level2Form(request.POST or None)
        if form_2.is_valid():
            if  request.POST['level2'] == "ctf-abcd1234efgh5678ijkl90":
                user_profile.pass_level('level2')
                return render(request,'home.html',{'level_progress':level_progress})
            
            
        form_3 = Level3Form(request.POST or None)
        if form_3.is_valid():
            if  request.POST['level3'] == "ctf-A3zH7WbXmFgY1sR8pU6qL5v":
                user_profile.pass_level('level3')
                return render(request,'home.html',{'level_progress':level_progress})
            
        form_4 = Level4Form(request.POST or None)
        if form_4.is_valid():
            if request.POST['level4']=='ctf:7e32a729b1226ed1':
                user_profile.pass_level('level4')
                return render(request,'home.html',{'level_progress':level_progress})
            
        form_5 = Level5Form(request.POST or None)
        if form_5.is_valid():
            if request.POST['level5'] == 'ctf:rCQ3edgh1!Db43fsas':
                user_profile.pass_level('level5')
                return render(request,'home.html',{'level_progress':level_progress})
            
        form_7 = Level7Form(request.POST or None)
        if form_7.is_valid():
            if request.POST['level7']=='ctf:1TSQ3afQ!@%Dl3k':
                user_profile.pass_level('level7')

                return render(request,'home.html',{'level_progress':level_progress})
   
            
            
    return render(request,'home.html', {'level_progress':level_progress})

def level1_view(request):
    return render(request,'level1/level1.html')


def level2_view(request):
    all_members = Member.objects.all
    return render(request,'level2/level2.html',{'all':all_members})

def level21_view(request):
    print(request.path)
    

    if request.method =='POST':
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('form submitted!'))
            return render(request,'level2/level2.html')
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            passwd = request.POST['passwd']
            email = request.POST['email']
            age = request.POST['age']

            messages.error(request,('please try again'))
            return render(request,'level2/level21.html',{'fname':fname,'lname':lname,'passwd':passwd,'email':email,'age':age})

        
    else:
        return render(request,'level2/level21.html')
    
    
def level22_view(request):
    if request.method == 'POST':
        form = Login_Member(request.POST or None)
        if form.is_valid():
            if request.POST['fname'] == 'admin' and request.POST['passwd'] == 'coolpassword':
                return HttpResponse('<h1>the code is -> ctf-abcd1234efgh5678ijkl90</h1>')
            else:
                messages.error(request,('please try again!'))
            return render(request,'level2/level22.html')
    return render(request,'level2/level22.html')


def level3_view(request):
    return render(request,'level3/level3.html')

def level31_view(request):
    if request.method == 'POST':
        form = Login_Member_level3(request.POST or None)
        if form.is_valid():
            if request.POST['fname']=='admin' and request.POST['passwd'] =='admin_cool_password':
                return HttpResponse('<h3>the flag = ctf-A3zH7WbXmFgY1sR8pU6qL5v</h3>')
            else:
                messages.error(request,('please try again'))
                return render(request,'level3/level31.html')
    return render(request,'level3/level31.html')




def level4_view(request):
    return render(request,'level4_file/level4.html')


        









class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"






