from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pictures/pikachoo.gif",upload_to='profile_pictures',blank=True,null=True)
    location = models.CharField(max_length=100)
    level_progress = models.JSONField(default={'level1': False, 'level2': False , 'level3': False ,'level4': False ,'level5': False ,'level6': False ,'level7': False ,'level8': False ,'level9': False }) 
    
    
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        # ... your custom logic ...
        super().save(*args, **kwargs)

        


 
        
    def pass_level(self, level):
        # Update the boolean value for the passed level
        print(self.level_progress)
        if level in self.level_progress:
            self.level_progress[level] = True
            self.save()
        else:
            raise ValueError("Invalid level")
        