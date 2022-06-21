# Generated by Django 4.0.4 on 2022-06-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateField()),
                ('department', models.CharField(choices=[('General Health', 'General Health'), ('Cardiology', 'Cardiology'), ('Dental', 'Dental'), ('Medical Research', 'Medical Research')], max_length=40)),
                ('mobileno', models.CharField(max_length=15)),
                ('msg', models.TextField()),
            ],
        ),
    ]