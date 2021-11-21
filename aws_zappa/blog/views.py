
   
from django.shortcuts import render


 
 

def homepage(request):
 
    contex = {
            "result": ""

    }
    return render(request, 'blog/homepage.html', contex)