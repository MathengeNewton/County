# Generated by Django 3.2.7 on 2021-09-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membershipNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('firstName', models.CharField(blank=True, max_length=200, null=True)),
                ('middleName', models.CharField(blank=True, max_length=200, null=True)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('emailAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('idNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('constituencies', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('institution', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]