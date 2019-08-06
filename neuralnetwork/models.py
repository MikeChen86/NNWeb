from django.db import models

# Create your models here.


class UploadImage(models.Model):
    image = models.ImageField(upload_to='upload_images/', verbose_name='上傳圖片', blank=False, null=False)

    def __str__(self):
        return self.image.name
