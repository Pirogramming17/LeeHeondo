from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length= 100, verbose_name="제목")
    open_date = models.CharField(max_length= 50, verbose_name="개봉연도")
    
    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('THRILLER', 'Thriller'),
        ('ROMANTIC', 'Romantic'),
        ('SF', 'SF'),
        ('DRAMA', 'Drama'),
        ('ANIMATION', 'Animation'),
        ('ADVENTURE', 'Adventure'),
        ('FANTASY', 'Fantasy'),
        ('HORROR', 'Horror'),
        ('MYSTERY', 'Mystery'),
        ('DOCUMENTARY', 'Documentary'),
        ('CHOICE', '선택'),

    ]
    genre = models.CharField(
        max_length= 20, verbose_name="장르",choices = GENRE_CHOICES,
        default = 'CHOICE'
    )

    star = models.FloatField(max_length= 50, verbose_name="별점")
    running_time = models.IntegerField(verbose_name="러닝타임")
    running_hour = 0
    running_min = 0

    review = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length= 100, verbose_name="감독")
    actor = models.CharField(max_length= 100, verbose_name="배우")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
