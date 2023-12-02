from django.db import models


# Create your models here.
class Catalog(models.Model):
    name = models.CharField(verbose_name='Name of product', max_length=60)
    price = models.IntegerField(verbose_name='Price')
    photo = models.ImageField(verbose_name='Image of product', upload_to='photo/%Y/%m/%d/', default='/photo/2023/11/19/empty.png')
    description =  models.TextField(verbose_name="Description of product", default='')
    category  = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category', null=True)

    def __str__(self):
        return self.name 
        
class Category(models.Model):
    name = models.CharField(verbose_name='Name of category', max_length=60)
    
    def __str__(self):
        return self.name 


class Task(models.Model):
    title = models.CharField(verbose_name='Title' , max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class  Customer(models.Model):
    name = models.CharField(verbose_name='Name of customer' , max_length=60)
    email = models.EmailField(max_length=100 , null=True , blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(verbose_name='Name of author' , max_length=60)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(verbose_name='Title' , max_length=255)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, verbose_name='Author of book', max_length=60)
    
    def __str__(self):
        return self.title


