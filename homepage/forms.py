
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    
    error_messages = {
            'duplicate_username': ("exists dude"),
            'password_mismatch': ("The two password fields didn't match."),
        }
    def __init__(self, *args, **kwargs):
            super(UserCreateForm, self).__init__(*args, **kwargs)
            self.fields['username'].error_messages = {'invalid': 'This name is not a name!'}
            self.fields['password1'].error_messages = {'required': 'required, man'}
            
    
    email = forms.EmailField(required=True)



    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
        
    
    