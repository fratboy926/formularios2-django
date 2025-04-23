from django import forms
from .models import Pessoa


	        

         class formularioCadatro(forms.ModelForm):
	     # class meta:	
		      # model = Pessoa
		      # Fields = ('nome', 'email')
              nome = forms.CharField(max_length=50)
              email = forms.EmailField()
		 #numero = forms.NumberInput      

