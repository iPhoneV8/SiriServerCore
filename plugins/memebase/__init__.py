#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: cytec iamcytec@googlemail.com
#project: SiriServer
#german memebase plugin


from plugin import *
import urllib
from BeautifulSoup import BeautifulSoup
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine


class memebase(Plugin):

	res = {
		'latestmeme': {
			#'id-ID': '.*fenomena terbaru.*',
                        'de-DE': '.latest meme.*',
			'en-US': '.*latest meme.*'
		},
		'lasttroll': {
			'de-DE': '.*(problem|troll|trollface).*',
			'en-US': '.*(problem|troll|trollface).*'
                       #'id-ID': '.*(masalah|troll|trollface).*'
		},
		'fffuuu': {
			'de-DE': '.*(fuck|fffuuu|ficken|scheiße).*',
			'en-US': '.*(fuck|fffuuu|shit|fuck you).*'
                        #'id-ID': '.*(sialan|fffuuu|shit|sialan kau).*'
		},
		'yuno': {
			'de-DE': '.*(wieso|warum|y u no|why you no|why you know).*',
			'en-US': '.*(y u no|why you no|why you know|why you not).*'
                        #'id-ID': '.*(y u no|mengapa anda tidak|anda tidak|mengapa anda tahu|mengapa anda bukan).*'
		},
		'megusta': {
			'de-DE': '.*(me gusta|mag ich|i like).*',
			'en-US': '.*(me gusta|i like).*'
                        #'id-ID': '.*(saya gusta|saya suka).*'
		},
		'likeaboss': {
			'de-DE': '.*(like a boss|like boss|wie ein boss|wie ein schef).*',
			'en-US': '.*(like a boss|like boss).*'
                        #'id-ID': '.*(seperti seorang bos|seperti bos).*'
		},
		'likeasir': {
			'de-DE': '.*(like a sir|like sir|like a gentleman|wie ein gentleman|wie ein sir).*',
			'en-US': '.*(like a sir|like sir|like a gentleman).*',
                        #'id-ID': '.*(seperti bapak||seperti lelaki).*'
		}
	}

	#@register("id-ID", res['latestmeme']['id-ID'])
	@register("en-US", res['latestmeme']['en-US'])
	@register("de-DE", res['latestmeme']['de-DE'])
	def get_latestmeme(self, speech, language):
		html = urllib.urlopen("http://memebase.com")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("div", {"class": "content"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Latest Meme:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['lasttroll']['de-DE'])
	@register("en-US", res['lasttroll']['en-US'])
	#@register("id-ID", res['lasttroll']['id-ID'])
	def get_lasttroll(self, speech, language):
		html = urllib.urlopen("http://artoftrolling.memebase.com/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("div", {"class": "content"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Trollface",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['fffuuu']['de-DE'])
	@register("en-US", res['fffuuu']['en-US'])
	#@register("id-ID", res['fffuuu']['id-ID'])
	def get_fffuuu(self, speech, language):
		html = urllib.urlopen("http://ragecomics.memebase.com/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("div", {"class": "content"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Rage:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['yuno']['de-DE'])
	@register("en-US", res['yuno']['en-US'])
	#@register("id-ID", res['yuno']['id-ID'])
	def get_yuno(self, speech, language):
		html = urllib.urlopen("http://memebase.com/category/y-u-no-guy/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("div", {"class": "md"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Y U NO:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['megusta']['de-DE'])
	@register("en-US", res['megusta']['en-US'])
	#@register("id-ID", res['megusta']['id-ID'])
	def get_megusta(self, speech, language):
		html = urllib.urlopen("http://memebase.com/category/me-gusta-2/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("div", {"class": "md"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Me gusta",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['likeaboss']['de-DE'])
	@register("en-US", res['likeaboss']['en-US'])
	#@register("id-ID", res['likeaboss']['id-ID'])
	def get_likeaboss(self, speech, language):
		html = urllib.urlopen("http://memebase.com/category/like-a-boss-2/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("div", {"class": "md"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Like a Boss:",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE", res['likeasir']['de-DE'])
	@register("en-US", res['likeasir']['en-US'])
	#@register("id-ID", res['likeasir']['id-ID'])
	def get_likeasir(self, speech, language):
		html = urllib.urlopen("http://memebase.com/category/like-a-sir/")
		soup = BeautifulSoup(html)
		ImageURL = soup.find("div", {"class": "md"}).img["src"]
		view = AddViews(self.refId, dialogPhase="Completion")
		ImageAnswer = AnswerObject(title="Like a Sir",lines=[AnswerObjectLine(image=ImageURL)])
		view1 = AnswerSnippet(answers=[ImageAnswer])
		view.views = [view1]
		self.sendRequestWithoutAnswer(view)
		self.complete_request()
