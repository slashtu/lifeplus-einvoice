from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission, User
# forms
from einvoice.einvoice_forms import TerminalForm
from einvoice.einvoice_forms import G1Form


# Create your views here.

@login_required(login_url='/einvoice/login/')
def index(request):
    user = request.user
    permission = Permission.objects.get(codename='change_snippet')
    user.user_permissions.add(permission)

    username = request.user.username

    context_dict = { 'username': username }

    return render_to_response(
            'einvoice/base_index.html',
            context_dict,
            context_instance=RequestContext(request)
        )

@login_required(login_url='/einvoice/login/')
def addGroup1(request):

    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = TerminalForm(request.POST)
            # check whether it's valid:
#            if form.is_valid():
#                form.group_1_id = 1
#                form.group_2_id = 1
#
#                form.save()
#                # process the data in form.cleaned_data as required
#                # ...
#                # redirect to a new URL:
#                return HttpResponseRedirect('/einvoice/')

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

#def fb(request):
#    return render(request, 'einvoice/fb.html', '')