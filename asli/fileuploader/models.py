from django.db import models

# Create your models here.
class pic(models.Model):
    name = models.CharField(max_length=255, blank=True)
    pic = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    shar = models.BooleanField(default=False)
