from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pic = models.ImageField(upload_to='user/%y/%m') #연도별로 월별로 사진을 관리가 가능
    comment = models.TextField()
    point = models.IntegerField(default=0)

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/nopic.png/"