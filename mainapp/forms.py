from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import ( User, Rule)


class CompanySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        if commit:
            user.save()
        return user

class PolusSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1
        if commit:
            user.save()
        return user


class DepartmentSignUpForm(UserCreationForm):
    rules = forms.ModelMultipleChoiceField(
        queryset=Rule.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 3
        user.save()
        department = Rule.objects.create(user=user)
        department.rules.add(*self.cleaned_data.get('rules'))
        return user



class RuleModelForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['name','color']
