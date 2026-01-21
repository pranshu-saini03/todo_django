from django.db import models
class todo(models.Model):
    title =models.CharField(max_length=200)
    description = models.TextField()
    completed=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# Create your models here.
