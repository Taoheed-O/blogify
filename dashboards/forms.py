from django import forms
from blogs.models import Category


# Category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'