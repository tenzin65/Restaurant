from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# makemigration- creat changes and store in the file 
# migrate- apply the pending changes create by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()  # This should match the database column name
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

class Users(models.Model):
    username = models.CharField(max_length=122, unique=True)
    email = models.CharField(max_length=122, unique=True)
    password = models.CharField(max_length=128)  # Secure hash storage
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        """Hash the password before saving."""
        if not self.pk:  # Only hash password for new users
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Verify password."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
