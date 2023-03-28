from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=10000)
    content = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(default=timezone.now())
    image = models.ImageField(default='{title}.jpg', upload_to="snippet")
    
    def __str__(self):
        return f'{self.user.username} - Question'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)