from django.db import models


class ProductChoices(models.TextChoices):
    Electronics = 'Электроника'
    Clothing = 'Clothing'
    Beauty = 'Красота и здоровье'
    Home = 'Дом и интерьер'
    Sports = 'Спорт товары'
    Toys = 'Игрушки и игры'
    Books = 'Книги'
    AnimalProducts = 'Товары для животных'
