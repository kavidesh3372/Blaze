# Generated by Django 4.2.3 on 2023-07-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datetime', models.DateField()),
                ('High', models.FloatField()),
            ],
        ),
    ]
