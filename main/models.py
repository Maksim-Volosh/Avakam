from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=True)

    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        category = ''
        if self.parent:
            category = f'{self.parent.name} -> '
            if self.parent.parent:
                category = f'{self.parent.parent.name} -> {self.parent.name} -> '
        return f'{category}{self.name}:'
    
    def clean(self):
        if self.parent and self.parent.parent and self.parent.parent.parent:
            raise ValidationError({"parent": "Нельзя создать под-под-подкатегорию."})
    

class CategoryField(models.Model):
    category_field_id = models.AutoField(primary_key=True)
    FIELD_TYPES = [
        ('checkbox', 'Чекбоксы (множественный выбор)'),
        ('radio', 'Кнопки (один выбор)'),
        ('range', 'Диапазон (от-до)'),
    ]
    
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='fields'
        )    
    
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=True)

    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    options = models.TextField(
        help_text="Для 'checkbox' и 'radio' варианты через запятую. Для 'range' оставьте пустым.",
    )
    
    def __str__(self) -> str:
        return f"{self.name} <=> {self.slug}"