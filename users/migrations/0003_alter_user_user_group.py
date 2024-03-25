# Generated by Django 3.2.24 on 2024-03-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240310_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_group',
            field=models.CharField(choices=[('buyer', 'Покупатель'), ('vip', 'VIP'), ('regular', 'Постоянный клиент')], default='buyer', max_length=20),
        ),
    ]
