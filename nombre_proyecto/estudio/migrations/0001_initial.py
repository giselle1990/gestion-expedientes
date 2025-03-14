# Generated by Django 5.1.7 on 2025-03-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('objeto', models.CharField(max_length=255)),
                ('caratula', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
