# Generated by Django 3.2.8 on 2022-05-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0003_alter_product_proimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_user', models.CharField(max_length=20)),
                ('item_name', models.CharField(max_length=20)),
                ('item_price', models.FloatField()),
            ],
        ),
    ]
