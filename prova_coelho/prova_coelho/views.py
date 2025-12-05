from django.http import HttpResponse

# Colocar as views aqui
def teste_view(request):
    return HttpResponse('Apenas um teste')

def index_view(request):
    return HttpResponse('Bem-vindo ao site!')