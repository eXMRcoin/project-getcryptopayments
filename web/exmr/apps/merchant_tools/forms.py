from django import forms

from apps.merchant_tools.models import ButtonMaker


class ConvertRequestForm(forms.ModelForm):
    """
    Form used to save the coin requests
    """
    wallet_from = forms.CharField()
    wallet_to = forms.CharField()

    class Meta:
        model = CoinConvertRequest
        fields = ('wallet_from', 'wallet_to')


class NewCoinForm(forms.ModelForm):

	class Meta:
		model = NewCoin
		exclude = ['']
