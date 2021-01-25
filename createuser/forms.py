from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,unverified_user


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        # fields = '__all__'
        fields=('email','first_name','last_name')
        # exclude=('password','user_permissions','groups','date_joined','is_staff','is_superuser','last_login')
        # widgets = {
        #     'email': forms.TextInput(attrs={'class':'input-line full-width'}),
        #     'first_name':forms.TextInput(attrs={'class':'input-line full-width'}),
        #     'last_name':forms.TextInput(attrs={'class':'input-line full-width'}),
        #     'password1':forms.TextInput(attrs={'class':'input-line full-width'}),
        #     'password2':forms.TextInput(attrs={'class':'input-line full-width'})
        # }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

        

class registerForm(forms.ModelForm):
    password1=forms.CharField(max_length=20,label='confirm password')
    class Meta:
        model = unverified_user	 

        fields =['email','first_name','last_name','password','password1']

        widgets = {
            'email': forms.EmailInput(attrs={'id':'email'}),
        }

    def clean(self):


        super(registerForm, self).clean()
		
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        email=self.cleaned_data.get('email')

        if password !=password1:
            self._errors['password'] = self.error_class([
				'both password must be same'])
		
        ql=CustomUser.objects.filter(email=email).first()
        if ql:
            self._errors['email'] = self.error_class([
				'user already exist'])

        return self.cleaned_data
        