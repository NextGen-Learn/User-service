from django.core.exceptions import ValidationError
import re

def validate_email(data):
    email = data.get('email')
    if not email:
        raise ValidationError('Email is required')
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValidationError('Invalid email address')

def validate_password(data):
    password = data.get('password')
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters')

def custom_validation(data):
    validate_email(data)
    validate_password(data)
    return data
