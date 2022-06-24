from django.db import models

# Create your models here.





class Django(models.Model):

    Name=models.CharField(max_length=100,blank=True)
    # Last_name=models.CharField(max_length=100,blank=True)
    Age=models.IntegerField()
    Mobile=models.BigIntegerField(null=True)
    Email=models.EmailField(max_length=150,null=True)
    Username=models.CharField(max_length=100,blank=True)
    Password=models.CharField(max_length=20,null=True)

    # offer=models.BooleanField(default=False)

class Meta:
    db_table="appTest1_django"    
