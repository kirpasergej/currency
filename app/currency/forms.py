from django import forms

from currency.models import Rate, Source, ContactUS


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'currency_name',
            'sale',
            'buy',
            'source',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'name',
            'url',
            'phone',
        )


class ContactUSForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = (
            'email_from',
            'subject',
            'message',
        )
