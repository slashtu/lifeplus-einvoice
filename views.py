# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission, User
from django.contrib import messages
from django.views.generic import View


# models
from einvoice.models import Group_1, Employee

# forms
from einvoice.einvoice_forms import TerminalForm, G1Form, G2Form, RegisterForm
#from einvoice.einvoice_forms import UserCreateForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required(login_url='/einvoice/login/')
def index(request):
    user = request.user
    permission = Permission.objects.get(codename='change_snippet')
    user.user_permissions.add(permission)

    user = request.user
    username = user.username
    all_info = {}

    if user.is_superuser:
        all_info = Group_1.objects.all()

    context_dict = { 'user': user, 'info': all_info }

    return render_to_response(
            'einvoice/base_index.html',
            context_dict,
            context_instance=RequestContext(request)
        )

@login_required(login_url='/einvoice/login/')
def addGroup1(request):
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = G1Form(request.POST)
            # check whether it's valid:
            if form.is_valid():

                form.save()

                messages.success(request, u'新增成功 %s' % request.POST['name'])
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/einvoice/')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = G1Form()

    username = request.user.username

    context_dict = {
        'username': username,
        'form': form,
        }

    return render_to_response(
                'einvoice/base_g1.html',
                context_dict,
                context_instance=RequestContext(request)
            )


@login_required(login_url='/einvoice/login/')
def addTerminal(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TerminalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.group_1_id = 1
            form.group_2_id = 1

            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/einvoice/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = TerminalForm()

    username = request.user.username

    context_dict = {
        'username': username,
        'form': form,
        }

    return render_to_response(
            'einvoice/base_addterminal.html',
            context_dict,
            context_instance=RequestContext(request)
        )

@login_required(login_url='/einvoice/login/')
def forms(request):
    username = request.user.username
    context_dict = { 'username': username }
    return render_to_response(
            'einvoice/base_forms.html',
            context_dict,
            context_instance=RequestContext(request)
        )

@login_required(login_url='/einvoice/login/')
def tables(request):
    return render(request, 'einvoice/base_tables.html', '')


def login(request):
    return render(request, 'einvoice/login.html', '')


def logout_action(request):
    logout(request)
    return redirect('/einvoice/')


def register(request):

    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = UserCreationForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                user = form.save()
                acl = Employee( acl_group_id = 1, user_id = user.id)
                acl.save()

    else:
        form = UserCreationForm()

    context_dict = {
            'form': form,
            }

    return render_to_response(
            'einvoice/register.html',
            context_dict,
            context_instance=RequestContext(request)
           )

class RegisterSuperView( View ):
    pass

class RegisterManagerView( View ):
    pass

class RegisterStaffView( View ):

    def get(self, request):

        form = UserCreationForm()

        context_dict = { 'form': form}

        return render_to_response(
                'einvoice/base_register-staff.html',
                context_dict,
                context_instance=RequestContext(request)
            )

    def post(self, request):

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            acl = Employee( acl_group_id = 3, user_id = user.id)
            acl.save()

            return HttpResponseRedirect('/einvoice/')

        else:
            context_dict = { 'form': form}
            return render_to_response(
                        'einvoice/base_register-staff.html',
                        context_dict,
                        context_instance=RequestContext(request)
                    )

class Group2View( View):

    def get(self, request):

        username = request.user.username
        form = G2Form()

        context_dict = {
            'form': form,
            }

        return render_to_response(
                'einvoice/base_g2.html',
                context_dict,
                context_instance=RequestContext(request)
            )

    def post(self, request):

        form = G2Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/einvoice/')

        else:
            return render_to_response(
                        'einvoice/base_g2.html',
                        context_dict,
                        context_instance=RequestContext(request)
                    )

#def fb(request):
#    return render(request, 'einvoice/fb.html', '')