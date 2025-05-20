from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# makemigration- creat changes and store in the file 
# migrate- apply the pending changes create by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

# class Product(models.Model):

#     CATEGORY_CHOICES = [
#         ('Veg', 'Veg'),
#         ('Non-Veg', 'Non-Veg'),
#         ('Cold Drinks', 'Cold Drinks'),
#         ('Snacks', 'Snacks'),
#     ]

#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='product_images/')
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Correct usage

#     def __str__(self):
#         return self.name

from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('veg', 'Veg'),
        ('non_veg', 'Non-Veg'),
        ('cold_drinks', 'Cold Drinks'),
        ('snacks', 'Snacks'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


# class Users(models.Model):
#     username = models.CharField(max_length=122, unique=True)
#     email = models.CharField(max_length=122, unique=True)
#     password = models.CharField(max_length=128)  # Secure hash storage
#     phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         """Hash the password before saving."""
#         if not self.pk:  # Only hash password for new users
#             self.password = make_password(self.password)
#         super().save(*args, **kwargs)

#     def check_password(self, raw_password):
#         """Verify password."""
#         return check_password(raw_password, self.password)

#     def __str__(self):
#         return self.username

# class Userss(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name