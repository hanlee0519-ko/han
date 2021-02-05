from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # CASCADE 란? 유저가 사라지면, 프로필도 같이 삭제 / # related_name => request.user.profile , request.user.profile.nickname 사용을 위해

    image = models.ImageField(upload_to='profile/', null=True) # setting MEDIA_ROOT 에서 'media' 의 profile 에 이미지가 저장 # null = True 이미지 없어도 됨
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
