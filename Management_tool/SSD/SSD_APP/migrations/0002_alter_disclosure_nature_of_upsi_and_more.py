# Generated by Django 4.1.3 on 2023-01-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSD_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disclosure',
            name='Nature_of_UPSI',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='Purpose_of_sharing',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='Recipients_Id_Number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='Recipients_Id_Type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='Recipients_mobile_number',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='Recipients_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='Remark',
            field=models.CharField(max_length=254, null=True),
        ),
    ]