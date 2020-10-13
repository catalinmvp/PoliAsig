from django.shortcuts import render


def About_view(request):
     return render(request,'About/index.html')