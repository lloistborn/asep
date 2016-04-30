from django.shortcuts import render

import tweepy
from .stream_twitter import StreamTwitter

# Create your views here.
def index(request):
	title_page = 'Home'

	return render(request, 'asep/index.html', {
		'title_page' :	title_page,
		})

def stream(request):

	if request.method == 'POST':
		topic = request.POST['pesan']

		auth 	= tweepy.OAuthHandler("iJx3wTVeN0Kq9kw5Az3Dg", "ew0UH2mE7v3X8fXVNrviURsTG2KOtDR7wfOilgj2w")
		auth.set_access_token("89917052-4VPBIVRGLzPT7VNFXWm9mLX7Kq3IGsYDjLpRBXt7r", "Os1AGJ79g4MOhJLWJqvmDflhoZiUrlbP07TsPzkiBFc")
		api 	=tweepy.API(auth)
		sapi 	= tweepy.streaming.Stream(auth, StreamTwitter())
		sapi.filter(track=[topic])

		return render(request, 'app/result.html', {
			'title_page' 	: title_page,
			'result'		: result,
			})	

	return render(request, 'app/result.html', {
		'title_page' 	: title_page,
		'result'		: result,
			})	