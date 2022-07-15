from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date
class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True




class Product(BaseModel):
    image=models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255, default="blog")
    subcategory = models.TextField(default='uncatogrized')
    desc=models.TextField(blank=True, null=True)
    likes= models.ManyToManyField(User, related_name="blog_post", null=True, blank=True)
    post_date = models.DateField(auto_now_add=True)
    price=models.IntegerField()
    
   
    
    
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()
   








RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)

class Rating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  
    product=models.ForeignKey(Product, on_delete=models.CASCADE)  
    ratings=models.CharField(choices=RATING, max_length=125)