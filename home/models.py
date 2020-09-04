from django.db import models

# Create your models here.
class contact(models.Model):
    sno=models.AutoField(primary_key=True);
    name=models.CharField(max_length=30);
    email=models.EmailField();
    phone=models.IntegerField();
    content=models.TextField();
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
