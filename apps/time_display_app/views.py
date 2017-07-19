from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
	context = {
	"time": strftime("%H:%M %p", gmtime()),
	"day": strftime("%B %d, %Y", gmtime())
	}
	return render(request,'time_display_app/index.html',context)