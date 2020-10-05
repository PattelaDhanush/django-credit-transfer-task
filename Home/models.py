from django.db import models

# Create your models here.
class Members(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    credit= models.IntegerField()
class Tran(models.Model):
    s_name= models.CharField(max_length=100)
    r_name= models.CharField(max_length=100)
    t_credit= models.IntegerField()
    
