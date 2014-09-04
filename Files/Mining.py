import json, sys, time, Queue, operator, os, re
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from threading import Thread

reload(sys)
sys.setdefaultencoding('utf-8')

ckey = 'tq0pLyOfKAZaKFrYpOs96vmTE'
csecret = 'kl6HeOMPDMIHWE4v6gAPoVJOhBS0KBjPhs42ZWBv54N1zVvkdP'
atoken = '1206754410-h5O8JclBfXVLt55mO8S3uRcyNFzOjBDLyB7Apqc'
asecret = 'zdmzGhXqTjQVfGjrRw7YuNi7RxVTAPFeR0oMC7rL6ebD6'


locs = list()

#entries = Queue.Queue(1000)
theHash = {}
locked = False

class listener(StreamListener):
	seconds = ['pissed', 'miserable', 'misery', 'bad', 'isn\'t working', 'terrible', 'annoying', 'slow', 'damn', 'fucking', 'sucks']
	"""
	def on_data(self, data):
		global locs
		if not locked:
			dictionary = dict(json.loads(data))
			#print 'Incoming tweet : ' + dictionary['text']
			if set(self.seconds).intersection(dictionary['text'].split(' ')):
				print dictionary['text'].strip(), dictionary['coordinates']
				locs += [(dictionary['text'], dictionary['coordinates'])]
		coords = dictionary['coordinates']['coordinates']
		newPoint['lat'] = float(coords[0])
		newPoint['lon'] = float(coords[1])
		newPoint['text'] = dictionary['text']


		return True
		"""

	def on_status(self, status):
		global locs
		seconds = ['pissed', 'miserable', 'misery', 'bad', 'isn\'t working', 'terrible', 'annoying', 'slow', 'damn', 'fucking', 'sucks']
		#print status.text, status.coordinates
		if status.coordinates is not None and set(seconds).intersection(map(lambda x: x.lower(), status.text.split(' '))):
			print status.text
			locs += [(status.text, status.coordinates['coordinates'])]
		return True

	def on_error(self, status):
		print status
		return True

class worker(Thread):
	coordcount = 0
	def run(self):
		global locs
		while True:
			locked = True
			clear = lambda: os.system('clear')
			#clear()

			print self.coordcount
			for loc in locs:
				print loc 

			with open('coords.txt', 'a') as f:
				for entry in locs:
					self.coordcount += 1
					f.write(str(entry) + '\n')

			locs = list()
			locked = False
			time.sleep(5)

class waiter(Thread):
  def start(self):
  	keywords = ['internet', 'wifi']
  	auth = OAuthHandler(ckey, csecret)
  	auth.set_access_token(atoken, asecret)
  	twitterStream = Stream(auth, listener())
  	twitterStream.filter(languages = ['en'], track=keywords)
  	#languages=['en']
  	#35.206936, -97.444871
  	#[SWlongitude, SWLatitude, NElongitude, NELatitude]


worker().start()
#pusher().start()
waiter().start()