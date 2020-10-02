# from django.db import models
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User
# Create your models here

def validate_content(value):
    content = value 
    if content == "abc":
        raise ValidationError("Error cannot be ABC")
    return value
