from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control'
                                                           }))

    firstname = forms.CharField(max_length=40, label=False,
                                widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                              'class': 'form-control',
                                                              }))

    lastname = forms.CharField(max_length=40, label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                             'class': 'form-control',
                                                             }))
    password1 = forms.CharField(max_length=50,
                                required=True, label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True, label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    phone_number = forms.CharField(max_length=20, label=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Phone Number',
                                                                 'class': 'form-control',
                                                                 }))

    address = forms.CharField(max_length=30, label=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Address',
                                                            'class': 'form-control',
                                                            }))

    city = forms.CharField(max_length=30, label=False,
                           widget=forms.TextInput(attrs={'placeholder': 'City',
                                                         'class': 'form-control',
                                                         }))

    country = forms.CharField(max_length=30, label=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Country',
                                                            'class': 'form-control',
                                                            }))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        super().__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['firstname', 'lastname']
        help_texts = {
            'password1': None
        }


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password = forms.CharField(required=True, label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 }))
