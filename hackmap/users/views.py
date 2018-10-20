from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse


# Entry point for website
def index(request):
    context = {
        'signup_form': SignUpForm,
        'login_form': LoginForm,
    }
    return render(request, '../templates/index.html', context=context)


def map_view(request):

    if request.user.is_authenticated():
        pass


#
#
# Authentication
def auth_user(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')

            try:
                check_email = User.objects.get(email=email)
                return HttpResponse('Email already in use.')

                # TODO: Send message to form that user already exists
            except User.DoesNotExist:
                user = User.objects.create(None,
                                           form.cleaned_data.get('first_name'),
                                           form.cleaned_data.get('last_name'),
                                           form.cleaned_data.get('email'),
                                           form.cleaned_data.get('password'))
                user.save()
                return HttpResponse(status=200)

            except User.MultipleObjectsReturned:
                return HttpResponse(status=500)

        else:
            return HttpResponse("LoginForm is not valid", status=500)

    else:
        return render(request, '../templates/index.html', {'signup_form': SignUpForm(), 'login_form': LoginForm, })


def login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                snippet = User.objects.get(email=email)
                user = authenticate(email=email, password=password)
                login(request, user)

                return redirect('map')

            except User.DoesNotExist:

                return redirect('index')

        else:
            # TODO: send error message to login page
            pass

    else:
        redirect('index')
