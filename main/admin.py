from django.contrib import admin
from django.forms import formsets

from .forms import ListingDetailForm
from .models import (Category, CategoryField, City, Country, Listing,
                     ListingDetail)


class ListingAdmin(admin.ModelAdmin):
    form = ListingDetailForm

    list_display = ('title', 'price', 'category_id', 'user_id', 'created_at', 'active')
    search_fields = ['title', 'category_id__name']
    list_filter = ['category_id', 'price_type','created_at', 'active']

    fieldsets = (
        ("Основная информация", {
            'fields': (
                'title', 'description', 'image', 'price_type',  'condition', 'price', 'contact_number', 
                'contact_comment', 'country', 'city', 'category_id', 'user_id', 'custom_fields',
                       )
        }),
        ("Бустинг и закрепление", {
            'fields': ('boosted_at', 'boosts_remaining', 'is_pinned', 'pinned_duration')
        }),
        ("Дополнительно", {
            'fields': ('active', 'user_have_premium')
        }),
    )


    def save_model(self, request, obj, form, change):
        obj.save()
        form.save()

admin.site.register(Listing, ListingAdmin)
admin.site.register(Category)
admin.site.register(CategoryField)
admin.site.register(Country)
admin.site.register(City)
