from django import forms

class StartStopForm(forms.Form):
    print("************* at form")
    #opid = forms.CharField(widget=forms.HiddenInput())
    opid = forms.EmailField(required=False, widget=forms.HiddenInput(), initial="1")
    wid = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
    jcid = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
    running = forms.CharField(required=False, max_length=50, widget=forms.HiddenInput())
    #wid = forms.CharField(label='wid', max_length=100)
    #jcid = forms.CharField(label='jcid', max_length=100)
    #running = forms.CharField(label='running', max_length=100)
