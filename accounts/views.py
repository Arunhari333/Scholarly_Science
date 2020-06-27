from django.shortcuts import render

# Create your views here.
def register(request):
	return render(request,'register.html')

def detail(request):
	return render(request,'detail.html')
