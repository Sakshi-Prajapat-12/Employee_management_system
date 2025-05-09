from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.FloatField()
    email=models.EmailField(max_length=30)
    mobile=models.CharField(max_length=13,unique=True)
    #city=models.CharField(max_length=20)

class Meta:
    db_table = "empdata"

    