from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'contact[name ={self.name} phone={self.phone} email={self.email} message={self.message}]'