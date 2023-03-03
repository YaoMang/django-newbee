from django.db import models

from datetime import timedelta

# Create your models here.

# userBaseInfo
class userBaseInfo(models.Model):
    username = models.CharField(max_length=64)
    
    #not encrypted
    #This is the production in development, will delete in the future
    password = models.CharField(max_length=64)
    
    #encrypted key
    #login_key = models.CharField(max_length=1024)
    def __str__(self) -> str:
        return self.username

# server encrypt key
class serverUniversalKey(models.Model):
    time_generate = models.DateTimeField(auto_now_add=True)
    
    key_name = models.CharField(max_length=60)
    key_type = models.CharField(max_length=60)
    key_description = models.CharField(max_length=200)

    key_value = models.CharField(max_length=2048)

    def __str__(self) -> str:
        return self.key_name

# user security info
class userSecurityInfo(models.Model):
    userInfo = models.OneToOneField(userBaseInfo, on_delete=models.CASCADE)

    email = models.EmailField(max_length=64)
    phone_number = models.CharField(max_length=40)

    token_expire_duration = models.DurationField(default=timedelta(days=180))

# token activate and deactivate
class userTokenInfo(models.Model):
    userInfo = models.ForeignKey(userBaseInfo, on_delete=models.CASCADE)
    encryptInfo = models.ForeignKey(serverUniversalKey, on_delete=models.CASCADE)

    hostname = models.CharField(max_length=255)
    time_generate = models.DateTimeField(auto_now_add=True)
    time_lastuse = models.DateTimeField()

    tokenKey = models.CharField(max_length=16)
