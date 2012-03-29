#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *
import random
import re
import urllib2, urllib, uuid
import json
from urllib2 import urlopen
from xml.dom import minidom

class statsPlugin(Plugin):
    
    @register("en-US", ".*how.*many.*active.*connections.*")
    @register("id-ID", ".*berapa.*koneksi.*aktif.*")
    def currently(self, speech, language, matchedRegex):
        if language == 'id-ID':
            self.say("Saat ini ada {0} user yang terhubung".format(self.numberOfConnections()))
        else:
            self.say("Currently {0} clients connected".format(self.numberOfConnections()))
        self.complete_request()
          
