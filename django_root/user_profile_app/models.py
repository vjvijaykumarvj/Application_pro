from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(
        primary_key = True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='media')

class UserProfile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    salary = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(null=True,max_length=10)
    age = models.IntegerField(blank=True)

