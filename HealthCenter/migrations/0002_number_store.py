# Generated by Django 4.0.3 on 2022-06-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(max_length=15)),
                ('Solar_Generation_MU', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'Number_store',
            },
        ),
    ]
