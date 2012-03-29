#!/usr/bin/python
# -*- coding: utf-8 -*-
#Created by Erich Budianto (praetorians) and edited by Jimmy Kane to stable
#Needs to add error response for french and german

from plugin import *
import random
import re
import urllib2, urllib, uuid
import json
from urllib2 import urlopen
from xml.dom import minidom

class horoscope(Plugin):
	
        @register ("en-GB", "(Tell me the horoscope for [a-zA-Z]+)|(Horoscope for [a-zA-Z]+)|(Horoscope for [a-zA-Z]+)|(The horoscope for [a-zA-Z]+)")
	@register ("en-US", "(Tell me the horoscope for [a-zA-Z]+)|(Horoscope for [a-zA-Z]+)|(Horoscope for [a-zA-Z]+)|(The horoscope for [a-zA-Z]+)")
	@register ("fr-FR", "(Quel est mon horoscope pour [a-zA-Z]+)|(Horoscope pour [a-zA-Z]+)|(Horoscope pour [a-zA-Z]+)|(Votre horoscope pour [a-zA-Z]+)")
	@register ("id-ID", "(Bagaimana horoskop untuk [a-zA-Z]+)|(Horoskop untuk [a-zA-Z]+)|(Horoskop untuk [a-zA-Z]+)|(horoskop untuk [a-zA-Z]+)")
	def horoscope_zodiac(self, speech, language):
            if language == 'id-ID':
                zodiac = speech.replace('Bagaimana ','').replace('horoskop ','').replace('untuk ', '').replace('Horoskop','').replace('Horoscope','').replace('pour ', '').replace('Tell me the','').replace('for','').replace('The','').replace(' ','')
                print ("Zodiac: {0}".format(zodiac))
                linkurl = 'http://widgets.fabulously40.com/horoscope.json?sign=%s' % zodiac
                print linkurl
                req=urllib.urlopen(linkurl)
                full_json=req.read()
                full=json.loads(full_json)
	    else:
                zodiac = speech.replace('Quel est ','').replace('votre ','').replace('Votre ', '').replace('horoscope','').replace('Horoscope','').replace('pour ', '').replace('Tell me the','').replace('for','').replace('The','').replace(' ','')
                print ("Zodiac: {0}".format(zodiac))
                linkurl = 'http://widgets.fabulously40.com/horoscope.json?sign=%s' % zodiac
                print linkurl
                req=urllib.urlopen(linkurl)
                full_json=req.read()
                full=json.loads(full_json)
            try:
                self.say(full['horoscope']['horoscope'])
                
            except KeyError:
                if language == 'id-ID':
                    self.say("Maaf, Saya tidak menemukan horoskop untuk zodiac {0}".format(zodiac))
                else:
                    self.say("Sorry I did not find a horoscope for zodiac {0}".format(zodiac))
            self.complete_request()
