from __future__ import unicode_literals
from django.db import models

# this is where the database exists. So what ever you do is here 
# is saved in the database

"""
    I can use this model to add any data to the home page 
    Simply means to make the home page more dynamically if 
    requested 
"""
class Main(models.Model):
    
    name = models.CharField(max_length=30)
    about = models.TextField(default="")
    facebook = models.CharField(default="", max_length=120)
    twitter = models.CharField(default="", max_length=120)
    youtube = models.CharField(default="", max_length=120)
    links = models.CharField(default="", max_length=160)
    telephone = models.CharField(default="", max_length=20)
    
    def __str__(self):
        return self.name