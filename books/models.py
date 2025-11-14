from django.db import models
from django.conf import settings


class Book(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Ужасы', 'Ужасы'),
        ('Драма', 'Драма'),
        ('Роман', 'Роман'),
        ('Фэнтези', 'Фэнтези'),
        ('История', 'История'),
    )

    title = models.CharField(max_length=100, verbose_name='name')
    image = models.ImageField(upload_to='books/', verbose_name='image')
    description = models.TextField(verbose_name='opisanie')
    director = models.CharField(max_length=100, verbose_name='avtor', default='govnovoz')
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='genre')
    country = models.CharField(max_length=100, default='США', verbose_name='country')
    pages = models.PositiveIntegerField(verbose_name='page count', default=400)
    age = models.PositiveIntegerField(verbose_name='age +', default=22222)
    language = models.CharField(max_length=100, verbose_name='language')
    publishing_house = models.CharField(max_length=100, verbose_name='house', default='jopa press')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Review(models.Model):
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='4')
    comment = models.TextField()

    def __str__(self):
        return f'{self.book.title} - {self.rating}'