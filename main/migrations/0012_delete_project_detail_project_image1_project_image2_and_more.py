# Generated by Django 4.1.1 on 2022-10-03 15:14

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_project_detail_image2_project_detail_image3_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='project_detail',
        ),
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(blank=True, upload_to=main.models.image_upload_detail1),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, upload_to=main.models.image_upload_detail2),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, upload_to=main.models.image_upload_detail3),
        ),
        migrations.AddField(
            model_name='project',
            name='image4',
            field=models.ImageField(blank=True, upload_to=main.models.image_upload_detail4),
        ),
        migrations.AddField(
            model_name='project',
            name='url_link',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
