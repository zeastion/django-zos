from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from zuser.forms import UserForm, UserProfileForm


def index(request):

    return render(request, 'zuser/index.html',)


# Zuser Register

def user_register(request):

    global profile_form
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'zuser/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


# Zuser Login

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'zuser/success.html')
            else:
                return render(request, 'zuser/fail.html')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'zuser/fail.html')
    else:
        return render(request, 'zuser/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/zuser/')


@login_required
def user_restricted(request):
    return HttpResponse("Since you're logged in,you can see this text!")
