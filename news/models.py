from __future__ import unicode_literals
import os
import random
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.db import models
from .utils import unique_slug_generator
from django.utils.text import slugify
from django.urls import reverse
# for catergory purpose we can use this library
# https://django-mptt.readthedocs.io/en/latest/overview.html
# https://stackoverflow.com/questions/60120266/django-categories-and-subcategories
from mptt.models import MPTTModel, TreeForeignKey

# Get the file name extension with the file name
def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

# Now use the filename and extension and upload to the correct path in the server
def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}[ext]'.format(new_filename=new_filename, ext=ext)
    return "news/imgs/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

# Article that can be created on the site for users to use for expressing themselves 
class Article(models.Model):
    
    authur = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, unique=True)
    article = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    body = models.TextField(default="")
    time_stamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, max_length=300)
    image_url = models.TextField(default="-")
    category_name = models.CharField(max_length=50, default="-")
    category_id = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    # objects = ArticleManager()
    
    def __str__(self):
        return self.article
    
    # this function works when requesting using primary ID
    def get_absolute_url(self):
        return reverse('article_details', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    # this function works when requesting using SLUG
    def get_absolute_url(self):
        return reverse("article_details", kwargs={"slug": self.slug})

        
# ths is a good way to utilize slug for the purpose of using slug
# and until we figure out a new and better way we should use this way
def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(article_pre_save_receiver, sender=Article)

# class Category(MPTTModel):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(blank=True, unique=True)
#     parent = TreeForeignKey(
#         'self',
#         default= 1,
#         blank = True,
#         null = True,
#         related_name = 'child',
#         on_delete = models.CASCADE
#     )

#     class Meta:
#         unique_together = ('slug', 'parent')
#         verbose_name_plural = "categories"
        
#     def __str__(self):
#         full_path = [self.name]
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent
#         return '->'.join(full_path[::-1])  