# Generated by Django 1.11.26 on 2019-12-17 17:35


import course_discovery.apps.course_metadata.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0229_update_ofac_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorganization',
            name='banner_image',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalorganization',
            name='certificate_logo_image',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[django.core.validators.FileExtensionValidator(['png'])]),
        ),
        migrations.AddField(
            model_name='historicalorganization',
            name='logo_image',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[django.core.validators.FileExtensionValidator(['png'])]),
        ),
        migrations.AddField(
            model_name='organization',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to=course_discovery.apps.course_metadata.utils.UploadToFieldNamePath('uuid', path='organization/banner_images')),
        ),
        migrations.AddField(
            model_name='organization',
            name='certificate_logo_image',
            field=models.ImageField(blank=True, null=True, upload_to=course_discovery.apps.course_metadata.utils.UploadToFieldNamePath('uuid', path='organization/certificate_logos'), validators=[django.core.validators.FileExtensionValidator(['png'])]),
        ),
        migrations.AddField(
            model_name='organization',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to=course_discovery.apps.course_metadata.utils.UploadToFieldNamePath('uuid', path='organization/logos'), validators=[django.core.validators.FileExtensionValidator(['png'])]),
        ),
    ]
