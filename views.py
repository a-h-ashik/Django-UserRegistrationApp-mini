from django.shortcuts import render
from .forms import Registration
from .models import User

# Create your views here.
def registration(request):
  form = Registration()
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      password = form.cleaned_data['first_pass']
      reg = User(name=name, email=email, password=password)
      reg.save()

  else:
    form = Registration()

  return render(request, 'user_registration/form.html', {'form' : form})