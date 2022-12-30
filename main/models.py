from django.db import models
from datetime import date
# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name
class Photo(models.Model):
    photo = models.ImageField(upload_to='media/')
    photo1 = models.ImageField(upload_to='media/')

    def __str__(self):
        return str(self.id)
    
class About(models.Model):
    age = models.IntegerField(max_length=3)
    resident = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=11)

    def __str__(self):
        return self.address

class Service(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=300)
    year1 = models.CharField(max_length=100)
    year2 = models.CharField(max_length=100)

    text = models.TextField()

    def __str__(self):
        return self.title
class Skill(models.Model):
    name = models.CharField(max_length=100)
    persent = models.IntegerField()

    def __str__(self):
        return self.name
class Programming(models.Model):
    name = models.CharField(max_length=100)
    persent = models.IntegerField()

    def __str__(self):
        return self.name
class Language(models.Model):
    name = models.CharField(max_length=100)
    persent = models.IntegerField()

    def __str__(self):
        return self.name

class Aloqa(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.fname

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogTitle(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/blog/')
    data = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    

    def __str__(self):
        return self.title

class Comments(models.Model):
    
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.comment
