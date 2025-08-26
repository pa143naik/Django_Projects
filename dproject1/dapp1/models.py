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

# class emp_details(models.Model):
#     emp_id=models.IntegerField(default=0)
#     emp_name=models.CharField(max_length=100)
#     emp_salary=models.IntegerField()

#     def __str__(self):
#         return self.emp_name

class student_details(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField(max_length=11)

    def __str__(self):
        return self.name

class author(models.Model):
    author_name=models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class books(models.Model):
    # book_id=models.IntegerField(default=0)
    book_name=models.CharField(max_length=100)
    book_price=models.IntegerField()
    author=models.ForeignKey(author,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.book_name

    

    























