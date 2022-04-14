from django.shortcuts import render
from .models import data_umkm

# Create your views here.

def index (request):
	collect = data_umkm.objects.all()

	context = {
		'data' : collect,
	}


	return render(request, 'umkm/index.html', context)