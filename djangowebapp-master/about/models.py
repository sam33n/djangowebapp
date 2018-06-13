from django.db import models

class About_mod(models.Model):
    title  = models.CharField(max_length=50)
    thumbnail = models.ImageField(default='default.png', blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
