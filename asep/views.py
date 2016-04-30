from django.shortcuts import render

import tweepy
from .stream_twitter import StreamTwitter
# from .search_twitter import SearchTwitter
# Create your views here.
def index(request):
	title_page = 'Home'

	return render(request, 'asep/index.html', {
		'title_page' :	title_page,
		})

def stream(request):
	kicauan='null'
	print('tet')

	if request.method == 'POST':
		print('tetot')

		topic = request.POST['pesan']

		streams = StreamTwitter()
		print('error dak')
		kicauan, balasan, pos, neg, net = streams.stream(topic)

		return render(request, 'asep/result.html', {
			'title_page' 	: 'Home',
			'kicauan'		: kicauan,
			'balasan'		: balasan,
			'positif'		: pos,
			'negatif'		: neg,
			'netral'		: net,
			})	

	return render(request, 'asep/result.html', {
		'title_page' 	: 'Home',
		'result'		: kicauan,
			})	