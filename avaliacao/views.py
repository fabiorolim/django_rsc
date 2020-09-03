from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        rsc = request.POST['rsc']
        data = request.POST['data']

        context = {
            'nome': nome,
            'rsc': rsc,
            'data': data,
        }

        return render(request, 'titulo.html', context)

    return render(request, 'index.html')


def titulo(request):
    return render(request, 'titulo.html')
