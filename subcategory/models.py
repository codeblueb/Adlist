from __future__ import unicode_literals
from django.db import models

class Sub_Category(models.Model):
    
    name = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    category_id = models.IntegerField()
    
    def __str__(self):
        return self.name