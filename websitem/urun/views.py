from django.shortcuts import render

def urun_list(request):
    return render(request, 'urun_list.html', {})
