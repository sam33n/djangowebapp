from django.db import models

class Blog_mod(models.Model):
    comment   = models.TextField()
    email     = models.EmailField(max_length=50)
    name      = models.CharField(max_length=20)
    time      = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
