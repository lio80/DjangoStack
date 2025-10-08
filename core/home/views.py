from django.shortcuts import render
import core.utils.logging_utils as log

# Create your views here.
def home(request):
    log.log_i("Home view accessed")
    return render(request, 'home.html')