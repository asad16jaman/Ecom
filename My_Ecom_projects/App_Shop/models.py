from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=254)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Categories'

class Product(models.Model):
    mainimg=models.ImageField(upload_to='Product')
    name=models.CharField(max_length=264)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='category')
    privies_text=models.TextField(max_length=200,verbose_name='Privies Text')
    detail_text = models.TextField(max_length=1000,verbose_name='Detail Text')
    price=models.FloatField()
    old_price=models.FloatField(default=0.00)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-created','name']


