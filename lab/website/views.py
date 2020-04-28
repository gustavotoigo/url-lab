from django.shortcuts import render


def list_error(request):
    list_ = ['ProductName', 'companyName']
    data = {"name": 'Lista', 'lista_erros': list_}
    return render(request, 'index.html', data)


