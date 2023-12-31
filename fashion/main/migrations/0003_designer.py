# Generated by Django 4.2 on 2023-12-30 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo1', models.ImageField(upload_to='designers/photos/%Y/%m/%d')),
                ('photo2', models.ImageField(upload_to='designers/photos/%Y/%m/%d')),
                ('biography1', models.TextField()),
                ('biography2', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.brand')),
            ],
        ),
    ]
