from django.db import models

class ContactDetail(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    message = models.TextField()



    def __str__(self):
        return self.name


class ModelChecks:
    pass
