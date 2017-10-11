from django.conf import settings
from django.db import models
from django.utils.text import slugify
# from urllib import request
# from django.core.files.base import ContentFile


# Create your models here.


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    # 添加多对多关系(图片的喜欢)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        使用slugify函数在没有提供slug字段时根据给定的图片标题自动生slug,
        然后，我们保存了这个对象。
        我们自动生成slug，这样的话用户就不用自己输入slug字段了。
        """
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)



