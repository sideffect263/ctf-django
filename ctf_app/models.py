from django.db import models
from django.contrib.auth.models import AbstractUser

#for level 2 model member
from cryptography.fernet import Fernet
import rsa


class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    passwd= models.CharField(max_length=50)
    age = models.IntegerField()

    
    
    
  
    def __str__(self):
        
        publicKey, privateKey = rsa.newkeys(512)
        encMessage = rsa.encrypt(self.passwd.encode(), publicKey)
        

        return "\n fname: "+self.fname + " \n\n encripted password \n"+str(encMessage) + "\n"+str(privateKey)
    


    
class LevelsPassed(models.Model):
    level1 = models.CharField(max_length=50, default="")
    level2 = models.CharField(max_length=50, default="")
    level3 = models.CharField(max_length=50, default="")
    level4 = models.CharField(max_length=50, default="")
    level5 = models.CharField(max_length=50,default="")
    level6 = models.CharField(max_length=50,default="")
    level7 = models.CharField(max_length=50,default="")


    def __str__(self):
        return self.level1+" "+self.level2 + " "+self.level3 + " "+ self.level4 + " "+self.level5






