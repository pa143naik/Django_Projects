from django.db import models

# Create your models here.

# class Details(models.Model):
#     course_id=models.IntegerField(default=0)
#     course=models.CharField(max_length=30)
#     duration=models.IntegerField()
    
# class M_model(models.Model):
#     name=models.CharField(max_length=30)
#     age=models.IntegerField(default=0) 
#     location=models.CharField(max_length=100)

class emp_details(models.Model):
    emp_id=models.IntegerField(default=0)
    emp_name=models.CharField(max_length=100)
    emp_salary=models.IntegerField()

    def __str__(self):
        return self.emp_name

    

    























