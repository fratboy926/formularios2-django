from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Opção 1 (recomendada para views dentro do mesmo app)
from .forms import formularioCadastro
from formularios2.forms import formularioCadastro
# Opção 2 (para imports de outros apps)


def home(request):

	#return HttpResponse('teste')
	#return render (request, 'home.html')
	 form = formularioCadastro()
	 return render(request, 'home.html', {'form': form})


def processa_formulario(request):
	#return HttpResponse('teste')
	# nome = request.POST.get('nome')
	#email = request.POST.get('email')
	form = formularioCadastro(request.POST)
	if form.is_valid():
	   #nome = form.data['nome']
	   #email = form.data['email']
	   form.save()	
	#print(nome)
	#print(email)
	#mensagem = " login: " + nome + " seu email :" + email
	#return HttpResponse(mensagem)
	#return HttpResponse(f"{nome} {email}")
	return HttpResponse("salvo com sucesso")
	return HttpResponse("erro interno do sistema")
		

def cadastro_view(request):

     form = formularioCadastro()  # Agora vai funcionar
     return render(request, 'cadastro.html', {'form': form})


#def minha_view(request):
    #if request.method == 'POST':
        #form = formularioCadastro(request.POST)
        #if form.is_valid():
            # Processar os dados do formulário
            #return render(request, 'sucesso.html')
    #else:
        #form = formularioCadastro()
    
    #return render(request, 'cadastro.html', {'form': form})

  