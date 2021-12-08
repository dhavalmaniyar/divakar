from django.db import models
from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    comment=models.TextField()
    commentedOn= models.DateField(default=timezone.now())

    def __str__(self):
        return self.name + " ("+str(self.commentedOn)+") " 