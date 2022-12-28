from django.db import models

gender_choose = (
    ('M','Male'),('F','Female')
)



class Employee(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    salary = models.IntegerField()
    address = models.TextField()
    photo = models.ImageField(upload_to='media')
    pincode = models.CharField(max_length=6)
    phonenumber = models.CharField(max_length=10)
    gender = models.CharField(choices=gender_choose,max_length=1)

    def __str__(self):
        return self.name
