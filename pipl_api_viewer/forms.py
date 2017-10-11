from django import forms

class PIPLSearch(forms.Form):
    email = forms.CharField(label='Email', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email' }))
    raw_phone = forms.IntegerField(label='Phone', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone' }))
    first_name = forms.CharField(label='First Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name' }))
    last_name = forms.CharField(label='Last Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name' }))
    middle_name = forms.CharField(label='Middle Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name' }))
    country_code = forms.CharField(label='Country Code', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country Code (eg. US)' }))
    state = forms.CharField(label='State Code', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State Code (eg. TX)' }))
    city = forms.CharField(label='City', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City' }))
    username = forms.CharField(label='Username', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username' }))
    from_age = forms.CharField(label='Age', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Age' }))