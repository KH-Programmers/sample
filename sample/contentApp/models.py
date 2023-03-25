from django.db import models

# Create your models here.
class contentModel(models.Model):
    def __str__(self):
        return str(self.id)
    auto_name = ""
    Title = models.CharField(max_length=2000,null=False)
    text = models.TextField(null=False)
    date = models.DateTimeField()