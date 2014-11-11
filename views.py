from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/einvoice/login/')
def index(request):
#    if not request.user.is_authenticated():
#        return  redirect('/lifeplus/einvoice/login/')

    username = request.user.username

    context_dict = { 'username': username }

    return render_to_response(
            'einvoice/base_index.html',
            context_dict,
            context_instance=RequestContext(request)
        )

def forms(request):
    return render(request, 'einvoice/base_forms.html', '')

def tables(request):
    return render(request, 'einvoice/base_tables.html', '')

def login(request):
    return render(request, 'einvoice/login.html', '')

def logout_action(request):
    logout(request)
    return redirect('/einvoice/')

#def fb(request):
#    return render(request, 'einvoice/fb.html', '')