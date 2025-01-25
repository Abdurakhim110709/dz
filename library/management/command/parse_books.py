from django.core.management.base import BaseCommand
from library.parser import parse_books

class Command(BaseCommand):
    help = 'Парсит книги и сохраняет их в базе данных'

    def handle(self, *args, **kwargs):
        parse_books()
        self.stdout.write(self.style.SUCCESS('Книги успешно спарсены'))
