# Generated by Django 4.1.6 on 2023-02-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terrarium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=11, verbose_name='size')),
                ('material', models.CharField(max_length=200, verbose_name='material')),
                ('year_of_prod', models.CharField(max_length=4, verbose_name='year_of_prod')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
        ),
    ]