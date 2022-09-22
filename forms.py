from django import forms

class Registration(forms.Form):
  name = forms.CharField(max_length=25, 
                        error_messages={'required':'Enter your name.'})
  email = forms.EmailField(max_length=50, 
                          error_messages={'required': 'Enter your gmail.'})
  first_pass = forms.CharField(max_length=8, label='Password',
                              error_messages={'required': 'Enter your password.'}, widget=forms.PasswordInput)
  second_pass = forms.CharField(max_length=8, label='Re-enter Password',
                                error_messages={'required': 'Re-enter your password.'}, widget=forms.PasswordInput)
                                
  def clean(self):
    cleaned_data = super().clean()
    print(cleaned_data)
    data_name = self.cleaned_data.get('name')
    data_email = self.cleaned_data.get('email')
    data_pass1 = self.cleaned_data.get('first_pass')
    data_pass2 = self.cleaned_data.get('second_pass')

    # Validations for name
    if data_name != None:
      for i in data_name:
        if i in '!@#$%^&*[{()}]':
          raise forms.ValidationError(
              "You can not use these '!@#$%^&*[{()}]' characters in your username.")

    # Validations for email
    if data_email != None:
      if '@gmail.com' not in data_email:
        raise forms.ValidationError('Enter a valid Gmail account.')

    # Validation for unmatched password
    if data_pass1 != None and data_pass2 != None:
      if data_pass1 != data_pass2:
        raise forms.ValidationError('Password does not match!')
    