from django.shortcuts import render
from django.http import Http404
#...



def acessorios(request):
    try:
        return render(request, 'acessorios.html')
    except:
        raise Http404
        #or
        return redirect('your-custom-error-view-name', error='error messsage')

def item(request):
    try:
        return render(request, 'sub/ite1.html')
    except: 
        return render(request, 'erro.html')

