from django.db import models
from django.contrib.auth.models import User

class todoo(models.Model):
    srno = models.AutoField(primary_key=True,auto_created=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    