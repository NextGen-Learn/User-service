from django.db import models

class UserDefault(models.Model):
    id = models.AutoField(primary_key=True)  
    email = models.EmailField() 
    user_name = models.CharField(max_length=255)  
    phone_number = models.IntegerField() 
    avatar = models.URLField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    last_login = models.DateTimeField() 

    class Meta:
        db_table = 'UserDefault'
