from django import forms
from .models import Category

PRODUCT_CATEGORY = list() #[(1,"Mouse"),(2,"Headphones"),(3,"Keyboards")]
for i in range(Category.objects.all().count()):
    PRODUCT_CATEGORY.append((i+1, Category.objects.all()[i].name))
print(PRODUCT_CATEGORY)

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=60)
    price = forms.IntegerField()
    photo = forms.ImageField(required=False)
    description = forms.CharField()
    category = forms.TypedChoiceField(choices=PRODUCT_CATEGORY, coerce=str)

