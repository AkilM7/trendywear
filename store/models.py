from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)  # Optional image

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory_images/', blank=True, null=True)  # Optional image

    def __str__(self):
        return self.name

class Dress(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1)  # ✅ Requires SubCategory with id=1
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dresses/')  # Required

    def __str__(self):
        return self.name

