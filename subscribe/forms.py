from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields='__all__'
        #exclude=('first_name',)
        labels={
            'first_name':_('Enter First name'),
            'last_name':_('Enter Last name'),
            'email':_('Enter Email')
        }
        # help_texts={
        #     'first_name':_('Enter character only!!!')
        # }
        error_messages = {
            'first_name':{
                'required':_('You cannon move forward without first name')
            }
        }

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid Last Name")
#     return value
    

# class SubscribeForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100, required=False, label="Enter First Name", help_text="Enter character only!!!")
#     last_name = forms.CharField(max_length=100, validators=[validate_comma], label="Enter Last Name")
#     email = forms.EmailField(max_length=100, label="Enter Email")
