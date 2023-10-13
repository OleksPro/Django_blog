# Generated by Django 4.2.5 on 2023-10-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='shop_sizes',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large')], default='S', max_length=2),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Назва статті'),
        ),
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=1, verbose_name='Перегляди'),
        ),
    ]