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
from einvoice.models import Group_1, User_group, Group1_permission

# forms
from einvoice.einvoice_forms import TerminalForm, G1Form, G2Form, RegisterForm, SelectStoreForm, G1PermissionForm
from django.contrib.auth.forms import UserCreationForm

# einvoice
from einvoice.model_helper import Store

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
                acl = User_group( acl_group_id = 1, user_id = user.id)
                acl.save()

    else:
        form = UserCreationForm()

    context_dict = {
            'form': form,
            }

    return render_to_response(
            'einvoice/base_register-super.html',
            context_dict,
            context_instance=RequestContext(request)
           )

class RegisterSuperView( View ):

    def get( self, request):
        form = UserCreationForm( prefix='user')
        context_dict = {'user_form': form}

        return render_to_response(
                    'einvoice/base_register-super.html',
                    context_dict,
                    context_instance=RequestContext(request)
                   )

    def post( self, request):

        form = UserCreationForm( request.POST, prefix='user')

        if form.is_valid():
            user = form.save()
            acl = User_group( acl_group_id = 1, user_id = user.id)
            acl.save()
            messages.success(request, u'新增帳號成功 %s' % request.POST['user-username'])

            return HttpResponseRedirect('/einvoice/')

        else:
            context_dict = { 'user_form': form}

            return render_to_response(
                        'einvoice/base_register-super.html',
                        context_dict,
                        context_instance=RequestContext(request)
                            )


class RegisterManagerView( View ):

    def get( self, request):
        user_form = UserCreationForm( prefix='user')
        group1_form = G1PermissionForm( prefix='group1')

        context_dict = {
                        'user_form': user_form,
                        'group1_form': group1_form,
                       }

        return render_to_response(
                    'einvoice/base_register-manager.html',
                    context_dict,
                    context_instance=RequestContext(request)
                   )

    def post( self, request):

        form = UserCreationForm( request.POST, prefix='user')

        if form.is_valid():
            user = form.save()

            # save acl of user
            acl = User_group( acl_group_id = 2, user_id = user.id)
            acl.save()

            # save group1 of user
            print request.POST
            group = request.POST['group1-group_1']
            group1_permission = Group1_permission( group_1_id = group, user_id = user.id )
            group1_permission.save()

            messages.success(request, u'新增最高權限帳號成功 %s' % request.POST['user-username'])

            return HttpResponseRedirect('/einvoice/')

        else:
            context_dict = { 'user_form': form}

            return render_to_response(
                        'einvoice/base_register-manager.html',
                        context_dict,
                        context_instance=RequestContext(request)
                            )

class RegisterStaffView( View ):

    def get(self, request):

        user_form = UserCreationForm( prefix="user")
#        store_form = SelectStoreForm( prefix="store")

        tree = Store.getStoreTree(group1_id = 1)

        context_dict = { 'user_form': user_form,
                         'store_tree': tree,
                         }

        return render_to_response(
                'einvoice/base_register-staff.html',
                context_dict,
                context_instance=RequestContext(request)
            )

    def post(self, request):

        user_form = UserCreationForm( request.POST, prefix="user")
#        sotre_form = SelectStoreForm( request.POST, prefix="store")

        if user_form.is_valid():
            user = user_form.save()
            acl = User_group( acl_group_id = 3, user_id = user.id)
            acl.save()

            return HttpResponseRedirect('/einvoice/')

        else:
            context_dict = { 'user_form': user_form}
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

def tree(request):
    return render(request, 'einvoice/tree.html', '')

#def fb(request):
#    return render(request, 'einvoice/fb.html', '')