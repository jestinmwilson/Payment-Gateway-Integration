# Generated by Django 3.1.1 on 2021-02-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('amount', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('order_id', models.CharField(max_length=1000)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
