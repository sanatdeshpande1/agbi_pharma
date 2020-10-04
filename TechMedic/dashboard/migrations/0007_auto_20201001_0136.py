# Generated by Django 3.1.1 on 2020-09-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200930_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='allergies',
            field=models.CharField(default='nil', max_length=1000),
        ),
        migrations.AddField(
            model_name='drugs',
            name='hereditary_diseases',
            field=models.CharField(default='nil', max_length=2000),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='blood_pressure_req',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='comorbid_conditions',
            field=models.CharField(default='nil', max_length=2000),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='other_medications',
            field=models.CharField(default='nil', max_length=2000),
        ),
    ]
