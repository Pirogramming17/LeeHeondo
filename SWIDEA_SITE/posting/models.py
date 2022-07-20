from django.db import models

# Create your models here.

# created_at = models.DateTimeField(auto_now_add=True) 
# updated_at = models.DateTimeField(auto_now=True)

# class Idea(models.Model):
#     title = models.CharField(max_length=50, verbose_name="제목")
#     photo = models.ImageField(blank=True, upload_to='ideas/%Y%m%d', verbose_name="사진")
#     content = models.TextField(verbose_name="컨텐츠")
#     # 4. interest
#     # 5. devtools

class DevTool(models.Model):
    name = models.CharField(max_length=50, verbose_name="도구이름")
    kind = models.CharField(max_length=50, verbose_name="도구종류")
    description = models.TextField(verbose_name="도구설명")