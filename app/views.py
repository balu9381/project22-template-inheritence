from django.shortcuts import render

# Create your views here.
def balu(request):
    return render(request,'parent.html')

def bala(request):
    return render(request,'child.html')