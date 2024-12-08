import time
from django import forms
from .models import Listing, ListingDetail


class ListingDetailForm(forms.ModelForm):
    description = forms.CharField(max_length=500, required=True, label='Описание', widget=forms.Textarea)
    condition = forms.ChoiceField(choices=ListingDetail.CONDITON_CHOICES, required=True, label='Состояние')
    contact_number = forms.CharField(max_length=30, required=True, label='Контактный номер')
    contact_comment = forms.CharField(max_length=120, required=False, label='Комментарий')
    pinned_at = forms.DateTimeField(required=False, label='Дата закрепления')
    pinned_duration = forms.IntegerField(required=False, label='Продолжительность закрепления')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            try:
                listing_detail = self.instance.details
                self.fields['description'].initial = listing_detail.description
                self.fields['condition'].initial = listing_detail.condition
                self.fields['contact_number'].initial = listing_detail.contact_number
                self.fields['contact_comment'].initial = listing_detail.contact_comment
                self.fields['pinned_at'].initial = listing_detail.pinned_at
                self.fields['pinned_duration'].initial = listing_detail.pinned_duration
            except ListingDetail.DoesNotExist:
                pass
            
    def clean(self):
        """
        Custom validation to set price to null if price_type is 'free'.
        """
        cleaned_data = super().clean()
        price_type = cleaned_data.get('price_type')
        price = cleaned_data.get('price')
        category = cleaned_data.get('category_id')
        country = cleaned_data.get('country')
        city = cleaned_data.get('city')
        
        if category and category.parent and category.parent.parent is None:
            raise forms.ValidationError({"category_id": "Вы можете выбрать только под-подкатегорию."})
        
        if country != city.country:
            raise forms.ValidationError({"city": "Город должен принадлежать стране."})

        if (price_type == 'free' or price_type == 'сontract') and price is not None:
            cleaned_data['price'] = 0
        return cleaned_data

    def save(self, commit=True):
        # Save the Listing object without committing to get its id
        listing = super().save(commit=False)

        # Work with the ListingDetail object
        # Ensure the Listing is saved before getting or creating ListingDetail
        listing.save()  # Save Listing to ensure it has a primary key first
        listing_detail, created = ListingDetail.objects.get_or_create(listing_id=listing)

        # Update fields of ListingDetail
        listing_detail.description = self.cleaned_data.get('description')
        listing_detail.condition = self.cleaned_data.get('condition')
        listing_detail.contact_number = self.cleaned_data.get('contact_number')
        listing_detail.contact_comment = self.cleaned_data.get('contact_comment')
        listing_detail.pinned_at = self.cleaned_data.get('pinned_at')
        listing_detail.pinned_duration = self.cleaned_data.get('pinned_duration')

        # Save ListingDetail
        listing_detail.save()

        # Return the Listing object
        return listing


    class Meta:
        model = Listing
        fields = ('title', 'price_type', 'price', 'image', 'category_id', 'country', 'city', 'user_id', 'custom_fields')




