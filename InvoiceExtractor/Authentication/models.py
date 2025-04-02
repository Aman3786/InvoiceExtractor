from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False, serialize=False, verbose_name='ID')
    email = models.EmailField(unique=True, help_text="Unique Email for each user.")
    
    def __str__(self):
        return self.username + " | " + self.email