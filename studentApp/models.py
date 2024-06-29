from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_phone_number(value):
    if not  len(value) == 10  and not (ch.isdigit() for ch in value):
        raise ValidationError('Phone number number must contain 10 digits')
  

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(validators=[validate_phone_number], max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"