from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    size_length = models.FloatField()
    size_width = models.FloatField()
    size_height = models.FloatField()
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    parent_category_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, through='ProductCategory')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

