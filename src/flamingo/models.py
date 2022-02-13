from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "user"


class Information(models.Model):

    class Meta:
        db_table = "information"
        verbose_name = "Information"
        verbose_name_plural = "Information"

    title = models.CharField("タイトル", max_length=50)
    contents = models.TextField("内容", max_length=500)
    published_at = models.DateTimeField(null=True)


class Service(models.Model):

    class Meta:
        db_table = "services"
        verbose_name = "Service"
        verbose_name_plural = "Service"
        ordering = ['priority']

    code = models.CharField("code", max_length=10, unique=True)
    name = models.CharField("name", max_length=30)
    is_freemium = models.BooleanField("freemium", default=False)
    priority = models.IntegerField("priority",)
