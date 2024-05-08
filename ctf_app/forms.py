from django import forms
from django.http.response import HttpResponse
from django.contrib.auth import get_user_model
from .models import Member
from .models import LevelsPassed


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname','lname','email','passwd','age']
        
class Login_Member(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname','passwd']
        
class Login_Member_level3(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname','passwd']
        
   
class Level1Form(forms.ModelForm):
    class Meta:
        model = LevelsPassed
        fields =['level1']     
        
class Level2Form(forms.ModelForm):
    class Meta:
        model =LevelsPassed
        fields = ['level2']
        
class Level3Form(forms.ModelForm):
    class Meta:
        model = LevelsPassed
        fields = ['level3']
        
class Level4Form(forms.ModelForm):
    class Meta:
        model = LevelsPassed
        fields = ['level4']


class Level5Form(forms.ModelForm):
    class Meta:
        model = LevelsPassed
        fields = ['level5']
        
    
class Level6Form(forms.ModelForm):
    class Meta:
        model = LevelsPassed
        fields = ['level6']
        
class Level7Form(forms.ModelForm):
    class Meta:
        model = LevelsPassed
        fields = ['level7']