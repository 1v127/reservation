from django.shortcuts import render

# Create your views here.
def create_resume(request):
    return render(request, 'create_resume.html')