from django.db import models

# Create your models here.

# created_at = models.DateTimeField(auto_now_add=True) 
# updated_at = models.DateTimeField(auto_now=True)

class DevTool(models.Model):
    name = models.CharField(max_length=50, verbose_name="도구이름")
    kind = models.CharField(max_length=50, verbose_name="도구종류")
    description = models.TextField(verbose_name="도구설명")

class Idea(models.Model):

    # devtools = DevTool.objects.all()
    # devtool_list = [name for name in devtools]

    title = models.CharField(max_length=50, verbose_name="제목")
    photo = models.ImageField(blank=True, upload_to='ideas/%Y%m%d', verbose_name="사진")
    content = models.TextField(verbose_name="컨텐츠")
    interest = models.IntegerField(default=0, verbose_name="관심도")
    dev = models.CharField(max_length=50, verbose_name="예상 툴")

    created_at = models.DateTimeField(auto_now_add=True)

    # TOOL_CHOICES = devtool_list

    # tool = models.CharField(
    #     max_length=20, choices = TOOL_CHOICES, 
    # )
