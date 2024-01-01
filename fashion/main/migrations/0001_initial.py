# Generated by Django 4.2 on 2023-12-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('name_image', models.ImageField(upload_to='brands/titles/%Y/%m/%d')),
                ('image', models.ImageField(upload_to='brands/images/%Y/%m/%d')),
            ],
        ),
    ]
