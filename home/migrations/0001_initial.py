# Generated by Django 4.2.1 on 2023-05-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics/')),
                ('dsc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
