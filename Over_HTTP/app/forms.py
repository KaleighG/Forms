from django import forms  

class HelloForm(forms.Form):
    user_name = forms.CharField()

class AgeForm(forms.Form):
    endyear = forms.IntegerField()
    birthyear = forms.IntegerField()

class OrderForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()


