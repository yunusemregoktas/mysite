from django.shortcuts import render

def urun_list(request):
    return render(request, 'urun/urun_list.html', {})
