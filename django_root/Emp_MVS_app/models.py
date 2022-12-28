from django.core.validators import RegexValidator
from django.db import models
import uuid

pan_regex = RegexValidator(regex="[A-Z]{5}[0-9]{4}[A-Z]{1}", message="Please enter a valid  Pan number")
phone_regex = RegexValidator(regex="[0-9]{10}", message='Please Enter valid Phone Number')
pincode_regex = RegexValidator(regex="[0-9]{6}",message='Please Enter valid Pincode')

class Employee(models.Model):
    id = models.UUIDField(
        editable=False,default=uuid.uuid4,primary_key=True
    )
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    salary = models.IntegerField()
    address = models.TextField()
    photo = models.ImageField(upload_to='media')
    pincode = models.CharField(max_length=6,validators=[pincode_regex])
    mobile = models.CharField(max_length=10,validators=[phone_regex])
    pancard = models.CharField(max_length=10,validators=[pan_regex])

    def __str__(self):
        return self.name

