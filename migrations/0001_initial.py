# Generated by Django 4.2 on 2023-10-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, default='', max_length=250, unique=True)),
                ('title', models.CharField(default='Venture Project', max_length=250)),
                ('logo_color_version', models.ImageField(default='', upload_to='profile/%Y/%m/%d/', verbose_name='logo_color_version')),
                ('logo_white_version', models.ImageField(default='', upload_to='profile/%Y/%m/%d/', verbose_name='logo_white_version')),
                ('logo_height', models.IntegerField(default=60)),
            ],
        ),
    ]