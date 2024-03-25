from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    delivery_address = models.CharField(max_length=100)
    GROUP_CHOICES = [
        ('buyer', 'Покупатель'),
        ('vip', 'VIP'),
        ('regular', 'Постоянный клиент'),
    ]
    user_group = models.CharField(max_length=20, choices=GROUP_CHOICES, default='buyer')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



