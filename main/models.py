from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

from user.models import User


class Category(models.Model):
    """
    Categories model.

    This model contains categories for the listings in the application.

    A category can have a parent category, and this relationship is
    represented by the `parent` field.

    The `clean` method is used to validate that the category does not have
    more than two levels of nested categories.

    """
    
    # Base fields
    category_id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
        
    # Fields
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    # Relationships
    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE
    )
    
    # Methods
    def clean(self):
        if self.parent and self.parent.parent and self.parent.parent.parent:
            raise ValidationError({"parent": "Нельзя создать под-под-подкатегорию."})
        
    # Dunder methods
    def __str__(self) -> str:
        category = ''
        if self.parent:
            category = f'{self.parent.name} -> '
            if self.parent.parent:
                category = f'{self.parent.parent.name} -> {self.parent.name} -> '
        return f'{category}{self.name}:'
    
    # Meta
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
     

class CategoryField(models.Model):
    """
    CategoryField model.

    This model contains fields for categories in the application.

    Each field can have different types, such as checkboxes, radio buttons,
    and range fields. The `field_type` field is used to store the type of the
    field.

    The `options` field is used to store the options for the field. For
    example, if the field is a checkbox or a radio button, the options are
    stored as a comma-separated string.

    The category field is related to the category model, and this
    relationship is represented by the `category` field.

    """
    
    # Base fields
    category_field_id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    
    # Fields
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('Slug', max_length=50)
    FIELD_TYPES = [
        ('checkbox', 'Чекбоксы (множественный выбор)'),
        ('radio', 'Кнопки (один выбор)'),
        ('range', 'Диапазон (от-до)'),
    ]
    field_type = models.CharField('Тип поля', max_length=20, choices=FIELD_TYPES)
    options = models.TextField(
        'Варианты',
        help_text="Для 'checkbox' и 'radio' варианты через запятую. Для 'range' оставьте пустым.",
        max_length=250,
    )
    
    # Relationships
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='fields'
        )    
    
    # Dunder methods
    def __str__(self) -> str:
        return f"{self.name} <=> {self.slug}"
    
    # Meta
    class Meta:
        verbose_name = 'Category field'
        verbose_name_plural = 'Category fields'
    

class Country(models.Model):
    """
    Country model.

    This model contains countries in the Listing.

    """
    
    # Fields
    name = models.CharField('Страна', max_length=50)

    # Dunder methods
    def __str__(self):
        return self.name
    
    # Meta
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    """
    City model.

    This model contains cities in the Listing.

    """
    
    # Fields
    name = models.CharField('Город', max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name='Страна')

    # Dunder methods
    def __str__(self):
        return f"{self.name}, {self.country.name}"
    
    # Meta
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Listing(models.Model):
    """
    Listing model.

    This model contains listings in the application.

    A listing has a title, an image, a price type, a price, a country, a city,
    a category, and a user. The user is a foreign key to the User model.

    The `boost` method is used to boost the listing. Boosting the listing moves
    it to the top of the list, and it is only available for 3 times
    
    
    `is_pinned` field is used to mark the listing as pinned.
    A pinned listing is shown at the top of the list, and is only available 
    for users with the premium account.

    """
    
    # Base fields
    listing_id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    boosted_at = models.DateTimeField(blank=True, null=True)
    boosts_remaining = models.IntegerField(default=3)
    is_pinned = models.BooleanField(default=False)
    user_have_premium = models.BooleanField(default=False)
    custom_fields = models.JSONField('Дополнительные поля категории', blank=True, null=True)
    
    
    # Fields
    title = models.CharField('Название', max_length=70)
    image = models.ImageField('Фото', upload_to='listing/images')
    PRICE_TYPE_CHOICES = (
        ('fixed', 'Фиксированная цена'),
        ('сontract', 'Договорная цена'),
        ('free', 'Бесплатно'),
    )
    price_type = models.CharField('Тип цены', max_length=30, choices=PRICE_TYPE_CHOICES)
    price = models.IntegerField('Цена', null=True)
    
    # Relationships
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='listings', verbose_name='Страна')
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='listings', verbose_name='Город')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings', verbose_name='Категория')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listing_details', verbose_name='Пользователь')

    # Methods
    def boost(self):
        """
        Boost the listing.

        Boosting the listing moves it to the top of the list, and it is only
        available for 3 times. If the listing is already boosted, the boost
        is not available.

        Raises:
            ValueError: If no boosts remaining
        """
        if self.boosts_remaining > 0:
            self.boosted_at = now()
            self.boosts_remaining -= 1
            self.save()
        else:
            raise ValueError("No boosts remaining")

    # Dunder methods
    def __str__(self):
        return self.title
    
    # Meta
    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
    
    
class ListingDetail(models.Model):
    """
    Model for storing additional information about listings.
    
    This model provides additional details about a listing, such as
    description, condition, price type, and whether the listing is pinned or not.
    
    The 'pinned_at' and 'pinned_duration' fields are used to store the timestamp
    and duration of pinning, respectively.
    
    """
    # Base fields
    listing_detail_id = models.AutoField(primary_key=True)
    pinned_at = models.DateTimeField('Закреплено в', blank=True, null=True)
    pinned_duration = models.IntegerField('Продолжительность закрепления', blank=True, null=True)
    
    # Fields
    description = models.TextField('Описание', max_length=500)
    CONDITON_CHOICES = (
        ('new', 'Новый'),
        ('used', 'Б/у'),
        ('not_product', 'Не продукт'),
    )
    condition = models.CharField('Состояние', max_length=30, choices=CONDITON_CHOICES)
    contact_number = models.CharField('Контактый номер', max_length=30)
    contact_comment = models.CharField('Комментарий', max_length=120, blank=True, null=True)
    
    # Relationships
    listing_id = models.OneToOneField(Listing, on_delete=models.CASCADE, related_name='details', verbose_name='Объявление')
    
    # Meta
    class Meta:
        verbose_name = 'Listing Detail'
        verbose_name_plural = 'Listing Details'
