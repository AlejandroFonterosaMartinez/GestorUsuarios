from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User  
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def user_manager(request):
    users = User.objects.all()  
    return render(request, 'user_manager.html', {'users': users})


class CreateUserView(CreateView):
    model = User
    template_name = 'user_manager.html' 
    fields = ['username', 'email', 'password']  

    def get_success_url(self):
        return reverse_lazy('user_manager') 
    
def about(request):
    return render(request, 'about.html')
