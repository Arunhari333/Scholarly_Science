from django.shortcuts import render

# Create your views here.
def register(request):
	return render(request,'accounts/register.html')

def detail(request):
	return render(request,'accounts/detail.html')

