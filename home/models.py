from django.db import models

# Create your models here.
#things to know :
#mvt ie model views ra templates
#cms ie control model

#Creating a model  as required:

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    logo = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    url = models.URLField(max_length=500, blank=True)
    rank = models.IntegerField()
    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField()
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    slug = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', "rank")


class Feedback(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    comment = models.TextField()
    post = models.CharField(max_length=300)
    star = models.IntegerField()
    def __str__(self):
        return self.name



class SiteInfo(models.Model):
    add = models.TextField()
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=15)
    twitter = models.URLField(max_length=500, blank=True)
    facebook = models.URLField(max_length=500, blank=True)
    instagram = models.URLField(max_length=500, blank=True)
    linkedin = models.URLField(max_length=500, blank=True)
    youtube = models.URLField(max_length=500, blank=True)
    def __str__(self):
        return self.add

STOCK = (('In stock','In Stock'),('Out of Stock','Out of Stock'))
LABELS = (('default','default'),('hot','hot'),('new','new'),('sale','sale'))
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    slug = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100, choices=STOCK)
    labels = models.CharField(max_length=100, choices=LABELS)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', 'name', 'price')


class ProductReviews(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    date = models.DateField(auto_now=True)
    star = models.IntegerField()
    review = models.TextField()
    slug = models.SlugField(max_length=300)
    image = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.username



class Cart(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    slug = models.SlugField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.price

