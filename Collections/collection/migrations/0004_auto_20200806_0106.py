# Generated by Django 3.0.5 on 2020-08-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20200805_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitemmodel',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
