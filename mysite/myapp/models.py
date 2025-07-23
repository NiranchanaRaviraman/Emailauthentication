from django.db import models
from django.utils import timezone

# Create your models here.
class EmailVerify(models.Model):
    def __str__(self):
        return self.email
    
    email=models.EmailField(max_length=45)
    otp=models.IntegerField(null=True,blank=True)
    verify=models.BooleanField(default=False)
    otp_time=models.DateTimeField(default=timezone.now)