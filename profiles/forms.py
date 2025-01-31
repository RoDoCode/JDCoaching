from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'product_access', 'series_access')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            if field_name in placeholders:
                if field.required:
                    placeholder = f'{placeholders[field_name]} *'
                else:
                    placeholder = placeholders[field_name]
                field.widget.attrs['placeholder'] = placeholder
                field.widget.attrs['class'] = (
                    'border-black rounded-0 profile-form-input'
                )
                field.label = False
