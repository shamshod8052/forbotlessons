from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name="Telegram ID", unique=True, default=1)
    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"
