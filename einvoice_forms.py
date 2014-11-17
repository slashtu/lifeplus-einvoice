from django import forms
from django.forms import ModelForm, TextInput

# model
from einvoice.models import Terminal

#class TerminalForm(forms.Form):
#    store_name = forms.CharField(label='Store name', max_length=100)


class TerminalForm(ModelForm):
        class Meta:
           model = Terminal
           fields = ['name', 'address', 'terminal_no', 'group_1', 'group_2']
           widgets = {
                       'name': TextInput(attrs={'class': 'form-control'}),
                       'address': TextInput(attrs={'class': 'form-control'}),
                       'terminal_no': TextInput(attrs={'class': 'form-control'}),
                   }
