from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_phone_number(value):
    if not  len(value) == 10  and not value.isdigit():
        raise ValidationError('Phone number number must contain 10 digits')
  

class Student(models.Model):
    gender_choice={'male':'male','female':'female','other':'other'}
    roll_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,choices=gender_choice,default='male')
    phone_number=models.IntegerField(validators=[validate_phone_number], unique=True)


    def __str__(self):
        return self.name