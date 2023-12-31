# Generated by Django 4.2 on 2023-06-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='addressline1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='addressline2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='addressline3',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='city',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='buyers'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='state',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
