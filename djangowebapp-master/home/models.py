from django.db import models

class Homes(models.Model):
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField()
    picture = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
