from django.shortcuts import render

import tweepy
# from .stream_twitter import StreamTwitter
from .search_twitter import SearchTwitter
# Create your views here.
def index(request):
	title_page = 'Home'

	return render(request, 'asep/index.html', {
		'title_page' :	title_page,
		})

def stream(request):
	kicauan=''
	if request.method == 'POST':
		topic = request.POST['pesan']

		cari=SearchTwitter()
		kicauan=cari.SearchKicauan(topic)
		print(kicauan[0])

		return render(request, 'asep/result.html', {
			'title_page' 	: 'Home',
			'result'		: kicauan,
			})	

	return render(request, 'asep/result.html', {
		'title_page' 	: 'Home',
		'result'		: kicauan,
			})	