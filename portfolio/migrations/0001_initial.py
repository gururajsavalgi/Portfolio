# Generated by Django 5.0.3 on 2024-05-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('gmail', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('about1', models.TextField(default='')),
                ('about', models.TextField(default='')),
                ('link1', models.URLField(blank=True, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
                ('link3', models.URLField(blank=True, null=True)),
                ('link4', models.URLField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='portfolio/media/img/')),
                ('image', models.ImageField(default='', upload_to='portfolio/media/pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('link1', models.URLField(blank=True, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
                ('about', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('icon', models.TextField(default='')),
                ('color', models.TextField(default='')),
                ('name', models.TextField(default='')),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
