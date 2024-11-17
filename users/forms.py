from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from users.models import Customer


class CustomerCreateForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль:',
        widget=forms.PasswordInput(attrs={
            'class': 'form_block__input'
        }),
    )

    password_repeat = forms.CharField(
        label='Подтвердите пароль:',
        widget=forms.PasswordInput(attrs={
            'class': 'form_block__input',
        }),
    )

    class Meta:
        model = User
        fields = [User.username.field.name, User.email.field.name]
        labels = {
            User.username.field.name: 'Имя:',
            User.email.field.name: 'Эл. почта:'
        }
        widgets = {
            User.username.field.name: forms.TextInput(attrs={
                'class': 'form_block__input'
            }),
            User.email.field.name: forms.EmailInput(attrs={
                'class': 'form_block__input'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerCreateForm, self).__init__(*args, **kwargs)
        self.fields[User.email.field.name].required = True

    def clean(self, commit=True):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self):
        customer = User.objects.create_user(
            username=self.cleaned_data[User.username.field.name],
            password=self.cleaned_data['password'],
            email=self.cleaned_data[User.email.field.name],
        )

        customer_data = Customer.objects.create(user=customer)
        customer_data.save()


class CustomerImageForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [Customer.image.field.name]


class CustomerBalanceAddForm(forms.Form):
    amount = forms.IntegerField(min_value=1, max_value=100000, label='Сумма', initial=1, widget=forms.NumberInput(
        attrs={
            'class': 'form_block__input'
        })
    )

    def save(self, current_user):
        amount = self.cleaned_data['amount']
        customer_data = get_object_or_404(Customer, user=current_user.id)
        customer_data.balance += amount
        customer_data.save()
