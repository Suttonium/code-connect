from django                    import forms
from django.core.exceptions    import ValidationError
from django.utils.translation  import ugettext_lazy as _

from accounts.models.user import User


class UserRegistrationForm(forms.ModelForm):
    """
    The UserRegistrationForm handles storing the user's
    basic information when signing up for the application.
    """
    
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput()
    )

    password_confirmation = forms.CharField(
        label='Password Confirmation',
        required=True,
        widget=forms.PasswordInput()
    )

    class Meta:
        """
        The UserRegistrationForm.Meta class handles assigning
        the model being saved with this form and the fields being
        used during the instance's creation.
        """

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_username(self) -> str:
        username: str = self.cleaned_data['username']

        if len(username) == 0:
            raise ValidationError(_('Your username must be at least one character in length.'))
        
        return username

    def clean_first_name(self) -> str:
        first_name: str = self.cleaned_data['first_name']

        if len(first_name) == 0:
            raise ValidationError(_('Your first name must be at least one character in length.'))
        else:
            first_name = first_name.title()

        return first_name

    def clean_last_name(self) -> str:
        last_name: str = self.cleaned_data['last_name']

        if len(last_name) == 0:
            raise ValidationError(_('Your last name must be at least one character in length.'))
        else:
            last_name = last_name.title()

        return last_name

    def clean_email(self) -> str:
        email: str = self.cleaned_data['email']

        if len(email) == 0:
            raise ValidationError(_('Your email address must not be zero characters long.'))
        else:
            email = email.lower()
        
        return email

    def clean_password_confirmation(self) -> str:
        password              : str = self.cleaned_data['password']
        password_confirmation : str = self.cleaned_data['password_confirmation']

        if len(password) < 5 or len(password_confirmation) < 5:
            raise ValidationError(_('Your password must be at least X characters in length.'))
        else:
            if password != password_confirmation:
                raise ValidationError(_('Your password inputs do not match. Please re-enter your password information.'))

        return password_confirmation

    def save(self, commit: bool=True) -> User:
        user: User = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
