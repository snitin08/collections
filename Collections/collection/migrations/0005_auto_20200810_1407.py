# Generated by Django 3.0.5 on 2020-08-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20200806_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitemmodel',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/photos/'),
        ),
    ]
