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

class Tutor(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    rating = models.FloatField()
    user_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    avatar = models.CharField(max_length=255)
    bio = models.TextField()
    education = models.TextField()
    verified = models.BooleanField()
    availability = models.JSONField()
    experience = models.TextField()
    photo = models.CharField(max_length=255)
    services = models.CharField(max_length=255)
    price = models.FloatField()
    video_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Репетитор'
        verbose_name_plural = 'Репетиторы'

    def __str__(self):
        return self.user_name
