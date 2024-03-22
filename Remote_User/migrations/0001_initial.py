# Generated by Django 5.0.1 on 2024-02-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRegister_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='detection_accuracy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='detection_ratio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='rainfall_estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date1', models.CharField(max_length=300)),
                ('Location', models.CharField(max_length=300)),
                ('MinTemp', models.CharField(max_length=300)),
                ('MaxTemp', models.CharField(max_length=300)),
                ('Rainfall', models.CharField(max_length=300)),
                ('Evaporation', models.CharField(max_length=300)),
                ('Sunshine', models.CharField(max_length=300)),
                ('WindGustDir', models.CharField(max_length=300)),
                ('WindGustSpeed', models.CharField(max_length=300)),
                ('WindDir', models.CharField(max_length=300)),
                ('WindSpeed', models.CharField(max_length=300)),
                ('Humidity', models.CharField(max_length=300)),
                ('Pressure', models.CharField(max_length=300)),
                ('Cloud', models.CharField(max_length=300)),
                ('Temp', models.CharField(max_length=300)),
                ('idnumber', models.CharField(max_length=300)),
                ('Prediction', models.CharField(max_length=300)),
            ],
        ),
    ]