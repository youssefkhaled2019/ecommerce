from django import forms
from .models import Account


class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Account
        fields=['first_name','last_name','email','phone_number','country']

    def __init__(self,*args,**kargs):
        super(RegisterForm,self).__init__(*args,**kargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter first name '
        self.fields['last_name'].widget.attrs['placeholder']='Enter last name'
        self.fields['email'].widget.attrs['placeholder']='Enter email '
        self.fields['phone_number'].widget.attrs['placeholder']='Enter phone_number '
        self.fields['password'].widget.attrs['placeholder']='Enter password '
        self.fields['confirm_password'].widget.attrs['placeholder']='Enter again password '


    def clean(self):
        clean_date=super(RegisterForm,self).clean()
        password=clean_date.get('password')
        confirm_password=clean_date.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError('password not match')
        
        return clean_date

"""

        return country_choices
    
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.CharField(max_length=100,unique=True)
    user_name=models.CharField(max_length=250,unique=True)
    phone_number=models.CharField(max_length=250)
    country=models.CharField(max_length=2,choices=get_country())#,default='US'
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']


"""        