# Generated by Django 4.1.5 on 2023-07-08 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[('Aventador', 'Aventador'), ('Gallardo', 'Gallardo'), ('Murcielago', 'Murcielago'), ('Agera', 'Agera'), ('Jesko', 'Jesko'), ('One:1', 'One:1'), ('La Ferrari', 'La Ferrari'), ('Stradale', 'Stradale'), ('F40', 'F40')], max_length=20)),
                ('manufacturer', models.CharField(choices=[('Lamborghini', 'Lamborghini'), ('Koenigsegg', 'Koenigsegg'), ('Ferrari', 'Ferrari')], max_length=20)),
                ('color', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue'), ('Orange', 'Orange'), ('Yellow', 'Yellow')], max_length=20)),
                ('manufacturing_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_app.address')),
            ],
        ),
    ]