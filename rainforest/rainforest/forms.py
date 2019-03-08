from rainforest.models import Product, Review
from django import forms
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    def clean(self):
        super().clean()
        description = self.cleaned_data.get('description')
        if len(description) < 10 or len(description) > 500:
            raise ValidationError('The body must be between 10-500 characters')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['comment']
