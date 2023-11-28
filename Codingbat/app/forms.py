from django import forms  

class FontForm(forms.Form):
    word = forms.CharField()
    num = forms.IntegerField()

class TeenForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()


class XyzForm(forms.Form):
    xyz = forms.CharField()
    

class AvgForm(forms.Form):
    num1 = forms.IntegerField()    
    num2 = forms.IntegerField()
    num3 = forms.IntegerField()
    num4 = forms.IntegerField()
    num5 = forms.IntegerField()
    num6 = forms.IntegerField()
    num7 = forms.IntegerField()
