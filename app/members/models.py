from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    content = models.TextField(blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
