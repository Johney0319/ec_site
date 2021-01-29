from django import forms
from .models import Jackets
from PIL import Image

class JacketsForm(forms.Form):
    SEX_CHOICES = (
        ('男性', '男性'),
        ('女性', '女性'),
        ('兼用', '兼用'),
    )

    SIZE_CHOICES = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    )

    BLAND_CHOICES = (
        ('クロクロ', 'クロクロ'),
        ('SARA', 'SARA'),
        ('UNITED JAPAN', 'UNITED JAPAN'),
    )

    jacket_name = forms.CharField(max_length=20)
    jacket_price = forms.CharField(max_length=10)
    jacket_size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    jacket_sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect,
        initial=0
    )
    jacket_bland = forms.ChoiceField(
        choices=BLAND_CHOICES,
    )
    jacket_image = forms.ImageField()

