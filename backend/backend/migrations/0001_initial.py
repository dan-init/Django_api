# Generated by Django 4.1.1 on 2023-06-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_side', models.CharField(max_length=100)),
                ('back_side', models.CharField(max_length=100)),
            ],
        ),
    ]
