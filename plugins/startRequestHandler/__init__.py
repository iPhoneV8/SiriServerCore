#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from plugin import *
from plugin import __criteria_key__

from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.systemObjects import DomainObject, ResultCallback
from siriObjects.websearchObjects import WebSearch

webSearchAnswerText = {"de": u"Das Web nach {0} durchsuchen …", "en": u"Searching the web for {0} …","zh": u"在網上搜索，{0} …", "id": u"mencari di internet untuk {0} …"}
webSearchAnswerFailureText = {"de": u"Entschuldigung, Ich, ich kann jetzt nicht das Web durchsuchen.", "zh": u"很抱歉，但我可以不搜索網站。", "en": u"Sorry but I cannot search the web right now.", "id": u"Maaf, saya tidak bisa melakukan pencarian saat ini."}
class startRequestHandler(Plugin):    

    #we should provide a shortcut for this....
    @register("de-DE", u"\^webSearchQuery\^=\^([a-z, ]+)\^\^webSearchConfirmation\^=\^([a-z]+)\^")     
    @register("en-US", u"\^webSearchQuery\^=\^([a-z, ]+)\^\^webSearchConfirmation\^=\^([a-z]+)\^")
    @register("en-AU", u"\^webSearchQuery\^=\^([a-z, ]+)\^\^webSearchConfirmation\^=\^([a-z]+)\^")
    @register("en-GB", u"\^webSearchQuery\^=\^([a-z, ]+)\^\^webSearchConfirmation\^=\^([a-z]+)\^")
    @register("id-ID", u"\^webSearchQuery\^=\^([a-z, ]+)\^\^webSearchConfirmation\^=\^([a-z]+)\^")
    @register("zh-CN", u"\^webSearchQuery\^=\^([a-z, ]+)\^\^webSearchConfirmation\^=\^([a-z]+)\^")
    @register("ru-RU", u"\^webSearchQuery\^=\^([a-z, ]+)\^\^webSearchConfirmation\^=\^([a-z]+)\^")
    def webSearchConfirmation(self, speech, language):
        # lets use a little hack to get that regex
        matcher = self.webSearchConfirmation.__dict__[__criteria_key__]['de-DE']
        regMatched = matcher.match(speech)
        webSearchQuery = regMatched.group(1)
        webSearchConfirmation = regMatched.group(2)
        
        lang = language.split("-")[0]

        resultCallback1View = UIAddViews(refId="")
        resultCallback1ViewView = UIAssistantUtteranceView()
        resultCallback1ViewView.dialogIdentifier="WebSearch#initiateWebSearch"
        resultCallback1ViewView.text=webSearchAnswerText[lang].format(u"„{0}“".format(webSearchQuery))
        resultCallback1ViewView.speakableText=webSearchAnswerText[lang].format(webSearchQuery)
        resultCallback1View.views = [resultCallback1ViewView]
        
        search = WebSearch(refId="", aceId="", query=webSearchQuery)
        resultCallback3View = UIAddViews(refId="")
        resultCallback3ViewView = UIAssistantUtteranceView()
        resultCallback3ViewView.dialogIdentifier="WebSearch#fatalResponse"
        resultCallback3ViewView.text=webSearchAnswerFailureText[lang]
        resultCallback3ViewView.speakableText=webSearchAnswerFailureText[lang]
        resultCallback3View.views=[resultCallback3ViewView]
        resultCallback3 = ResultCallback(commands=[resultCallback3View])
        search.callbacks = [resultCallback3]

        resultCallback2 = ResultCallback(commands=[search])
        resultCallback1View.callbacks = [resultCallback2]

        self.complete_request(callbacks=[ResultCallback(commands=[resultCallback1View])])
    
