from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=200, null=True)
    last_name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email

