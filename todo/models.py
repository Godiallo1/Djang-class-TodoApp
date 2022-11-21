from django.db import models

# Create your models here.

class Mytodo(models.Model):
    task = models.CharField(max_length= 250, null= False)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task