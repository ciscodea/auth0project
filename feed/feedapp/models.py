from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)
    date_hidden = models.DateTimeField(blank=True, null=True)
    hidden_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        blank=True, null=True, related_name='mod_who_hid')

    def __str__(self):
        return self.text


class Report(models.Model):
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

