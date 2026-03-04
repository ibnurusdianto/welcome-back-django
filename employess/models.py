from django.db import models



# Create your models here.

# implementasikan model employee 
class employee(models.Model):
    name = models.CharField(max_length=100) # charfield adalah karakter field
    age = models.IntegerField() # integerfield adalah integer field
    salary = models.IntegerField() # integerfield adalah integer field
    photo = models.ImageField(upload_to='photos/') # imagefield adalah image field
    designation = models.CharField(max_length=100) # charfield adalah karakter field
    email_address = models.EmailField(max_length=100, unique=True) # emailfield adalah email field
    phone_number = models.CharField(max_length=15, unique=True) # charfield adalah karakter field
    address = models.TextField() # textfield adalah text field
    created_at = models.DateTimeField(auto_now_add=True) # datetimefield adalah datetime field
    updated_at = models.DateTimeField(auto_now=True) # datetimefield adalah datetime field
    
    # untuk menampilkan nama employee di admin
    def __str__(self):
        return self.name
    
    
    
