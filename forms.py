from django import forms
from .models import Pessoa
#class formularioCadastro(forms.Form):  # Note o nome exato da classe
    #nome = forms.CharField(max_length=100)
    #email = forms.EmailField()

      

class formularioCadastro(forms.ModelForm):
       class Meta:
 	      model = Pessoa
 	      fields = ('nome' ,'email')




