from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from zuser.forms import UserForm, UserProfileForm


def index(request):

    return render(request, 'zuser/index.html',)


# Zuser Register

def user_register(request):

    registered = False
    error = []

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        password = request.POST.get('password', )
        conpassword = request.POST.get('conpassword', )

        if password != conpassword:
            error.append('Type the same passwords')

        else:
            if user_form.is_valid() and profile_form.is_valid():

                user = user_form.save()
                print 1, conpassword, 2
                user.set_password(conpassword)
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

    return render(request, 'zuser/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, })#'error': error})


# Zuser Login

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'zuser/index.html')
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
