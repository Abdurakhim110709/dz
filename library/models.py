from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    email = models.EmailField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    video_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        return self.review_set.all()



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