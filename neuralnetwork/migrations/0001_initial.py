# Generated by Django 2.1.7 on 2019-08-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload_images/', verbose_name='上傳圖片')),
                ('height', models.IntegerField(blank=True, default=0, null=True, verbose_name='圖片高度')),
                ('weight', models.IntegerField(blank=True, default=0, null=True, verbose_name='圖片寬度')),
            ],
        ),
    ]
