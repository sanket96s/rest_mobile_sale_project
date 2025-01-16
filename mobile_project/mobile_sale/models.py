from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class Reviews(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reviews_by_username')
    email = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reviews_by_email')
    reviews = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Review by {self.username}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    reviews = models.ManyToManyField(Reviews, blank=True)
    quantity = models.IntegerField()
    prod_image = models.ImageField(upload_to='products/', null=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField()