from django.db import models

# Create your models here.
class accounts(models.Model):
     
     name=models.CharField(max_length=50,null=False)
     email = models.EmailField(max_length=254,null=False)
     passwod=models.IntegerField(null=False)
     dob = models.DateField(null=False)
     post = models.CharField(max_length=50,null=False)
     def __str__(self) ->str :
         return self.name
     