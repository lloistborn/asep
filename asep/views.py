from django.shortcuts import render

# Create your views here.
def index(request):
	title_page = 'Home'

	return render(request, 'asep/index.html', {
			'title_page' :	title_page,
		})

def stream(request):
	return 0