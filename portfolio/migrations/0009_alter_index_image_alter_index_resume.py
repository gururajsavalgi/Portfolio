# Generated by Django 5.0.3 on 2024-05-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_index_image_alter_index_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='image',
            field=models.ImageField(default='', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='index',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
    ]