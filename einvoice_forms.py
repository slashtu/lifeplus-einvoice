# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput, Select
from django.contrib.auth.forms import UserCreationForm


# model
from django.contrib.auth.models import User
from einvoice.models import Terminal, Group_1, Group_2, Employee, Group1_permission


#class TerminalForm(forms.Form):
#    store_name = forms.CharField(label='Store name', max_length=100)

class RegisterForm( UserCreationForm ):
    class Meta:
            model = User
            fields = ['username', 'password1', 'password2']
            widgets = {
                       'username': TextInput(attrs={'class': 'form-control'}),
                       'password1': TextInput(attrs={'class': 'form-control'}),
                       'password2': TextInput(attrs={'class': 'form-control'}),
                               }

class TerminalForm(ModelForm):
        class Meta:
           model = Terminal
           fields = ['name', 'address', 'terminal_no', 'group_1', 'group_2']
           widgets = {
                       'name': TextInput(attrs={'class': 'form-control'}),
                       'address': TextInput(attrs={'class': 'form-control'}),
                       'terminal_no': TextInput(attrs={'class': 'form-control'}),
                       'group_1': Select(attrs={'class': 'form-control'}),
                       'group_2': Select(attrs={'class': 'form-control'}),
                   }

class G2Form(ModelForm):
        class Meta:
           model = Group_2
           fields = ['name', 'group_1']
           widgets = {
                       'name': TextInput(attrs={'class': 'form-control'}),
                       'group_1': Select(attrs={'class': 'form-control'}),
                   }


class G1Form(ModelForm):
        class Meta:
           model = Group_1
           fields = ['name', 'ubn']
           widgets = {
                       'name': TextInput(attrs={'class': 'form-control'}),
                       'ubn': TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入八位數字'}),
                   }

class G1PermissionForm(ModelForm):
        class Meta:
           model = Group1_permission
           fields = ['group_1']
           widgets = {
                       'group_1': Select(attrs={'class': 'form-control'}),
                   }


class SelectStoreForm( forms.Form ):
        selected = forms.BooleanField(required=False)

#class UserCreateForm(UserCreationForm):
#    email = forms.EmailField(required=True)
#
#    class Meta:
#        model = User
#        fields = ( "username", "email" )