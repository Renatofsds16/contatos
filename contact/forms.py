from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForms(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'seu nome'}
        ),
        label='primeiro nome'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'sobrenome'}
        ),
        label='sobrenome'
    )

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
        )
        widgets = {'first_name': forms.TextInput(attrs={
            'placeholder': 'escreva aqui'
        })}

    def clean(self):
        # cleaned_data = self.cleaned_data
        # self.add_error(
        #    'first_name', ValidationError('erros a corregir', code='invalid')
        # )
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'abc' or first_name == 'ABC':
            raise ValidationError('nome invalido')
        print('passei no first_name')
        return first_name
