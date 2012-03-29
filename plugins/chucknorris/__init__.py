import urllib2
import json

from plugin import *
class chucknorrisjoke(Plugin):

	@register ("en-US", ".*Chuck.*norris.*joke.*")
	@register ("id-ID", ".*Lelucon.*cuk.*noris.*")
	def st_chucknorris(self, speech, language):
		if language == 'id-ID':
			req = urllib2.Request("http://api.icndb.com/jokes/random")
		full_json = urllib2.urlopen(req).read()
		load = json.loads(full_json)
		store = load['value']['joke']
		store = store.replace('&quot;','\"')
		self.say(store)
		self.complete_request()
