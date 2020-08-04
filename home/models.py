from django.db import models

# Create your models here.

class TodoList(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.text