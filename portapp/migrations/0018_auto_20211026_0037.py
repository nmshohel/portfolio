# Generated by Django 3.1.4 on 2021-10-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0017_auto_20210103_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksection',
            name='work_index_photo',
            field=models.ImageField(blank=True, help_text='Upload 400x400 images to get a good look.', null=True, upload_to=''),
        ),
    ]