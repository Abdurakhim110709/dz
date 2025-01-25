import requests
from .models import Book
from django.core.files.images import ImageFile
from io import BytesIO


def parse_books():
    url = "https://openlibrary.org/subjects/science.json?limit=10"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        books = data['works']

        for book in books:
            title = book.get('title', 'No title')
            author = ', '.join([author['name'] for author in book.get('authors', [])])
            description = book.get('description', {}).get('value', 'No description available')
            price = 'N/A'
            cover_id = book.get('cover_id')

            image_url = None
            if cover_id:
                image_url = f"https://covers.openlibrary.org/b/id/{book['cover_id']}-L.jpg" if 'cover_id' in book else None



            Book.objects.create(
                title=title,
                author=author,
                description=description,
                price=price,
                image=image_url if image_url else None,  # Если изображения нет, оставляем поле пустым
            )
