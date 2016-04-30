from django.shortcuts import render

from .streamtwitter import StreamTwitter

# Create your views here.
def index(request):
	title_page = 'Home'

	return render(request, 'asep/index.html', {
			'title_page' :	title_page,
		})

def stream(request):
	if request.method == 'POST':

		msg = request.POST['pesan']

		st = new StreamTwitter()

    return render(request, 'app/result.html', {
		'title_page' 	: title_page,
		'result'		: result,
		})	