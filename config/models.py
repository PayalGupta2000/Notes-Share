from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class  User(AbstractUser):
    phone_number=models.CharField(max_length=15)

class Notes(models.Model):
    type_of_notes=(('Audio','Audio'),('Text','Text'),('Video','Video'))

    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    notes_type=models.CharField(choices=type_of_notes,max_length=20)
    file=models.FileField(upload_to="media")
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
class Share_Notes(models.Model):
    notes=models.ManyToManyField(Notes,related_name="notes_share")
    sender=models.ForeignKey(User,on_delete=models.CASCADE)
    shared_timing=models.DateTimeField(auto_now_add=True)
    shared_with=models.ManyToManyField(User,related_name="notes_receiver")

   