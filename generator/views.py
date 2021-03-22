from django.shortcuts import render

# Create your views here.
def guest_resume(request):
    return render(request, 'guest_resume.html')
