from django import forms


class UserForm(ModelForm):
    class Meta:
        model=User
    