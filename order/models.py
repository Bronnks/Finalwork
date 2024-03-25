from django.db import models
from django.db.models import F
from users.models import User
from product.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('paid', 'Оплата'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]

    PAYMENT_CHOICES = [
        ('card', 'Карта'),
        ('cash', 'Наличные'),
        ('erip', 'ЕРИП'),
        ('qr', 'QR-код'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_after_discount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='card')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True)

    @classmethod
    def create(cls, user, discount, **kwargs):
        if user.group == 'vip':
            discount = 0.2  # 20% скидка для VIP пользователей
        elif user.group == 'regular':
            discount = 0.1  # 10% скидка для Постоянных клиентов
        else:
            discount = 0

        return cls.objects.create(user=user, discount=discount, **kwargs)


class OrderList(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=F('product__price'))
    quantity = models.IntegerField()
