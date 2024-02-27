from django.db import models

class TodoProj(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    finished=models.BooleanField(default=True)

    
