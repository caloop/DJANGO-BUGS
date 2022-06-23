from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages    





def contato_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Eviado com sucesso!')
                form = ContactForm()
                return render(request, 'contato.html', {'form': form})
        else:
                 messages.add_message(request, messages.ERROR, 'Sem sucesso!')
                 return render(request, 'contato.html')
 
    return render(request, 'contato.html')


                






