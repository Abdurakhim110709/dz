from django.db import models


class Book(models.Model):
    GENRE_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Романтика', 'Романтика'),
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='book_images/', verbose_name='Изображения', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    genre = models.CharField(choices=GENRE_CHOICES, max_length=20, verbose_name='Жанр')
    email = models.EmailField(verbose_name='Email')
    author = models.CharField(max_length=100, verbose_name='Автор')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книга'


class Review(models.Model):
     STATUS_CHOICES = (
         ('🌟', '🌟'),
         ('🌟🌟', '🌟🌟'),
         ('🌟🌟🌟', '🌟🌟🌟'),
         ('🌟🌟🌟🌟', '🌟🌟🌟🌟'),
         ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'),
     )
     stars = models.CharField(choices=STATUS_CHOICES, max_length=10, verbose_name='Оценка')
     comemnt = models.TextField(verbose_name='Коментарии')
     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

     def __str__ (self):
         return self.book.title

     class Meta:
         verbose_name = 'Отзыв'
         verbose_name_plural = 'Отзыв'