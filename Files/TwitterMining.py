import json
import sys
import time
import plistlib
import Queue
import ftplib
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from threading import Thread

reload(sys)
sys.setdefaultencoding('utf-8')

twitterckey = 'tq0pLyOfKAZaKFrYpOs96vmTE'
twittercsecret = 'kl6HeOMPDMIHWE4v6gAPoVJOhBS0KBjPhs42ZWBv54N1zVvkdP'
twitteratoken = '1206754410-h5O8JclBfXVLt55mO8S3uRcyNFzOjBDLyB7Apqc'
twitterasecret = 'zdmzGhXqTjQVfGjrRw7YuNi7RxVTAPFeR0oMC7rL6ebD6'

negatives = ['bad', 'terrible', 'horrendous', 'annoying', 'worst']
keywords = ["car", "parking", "lot", "Parking", "Car", "Lot", "Truck", "truck"]

entries = Queue.Queue(1000)

class listener(StreamListener):

	def on_data(self, data):
		dictionary = dict(json.loads(data))
		if('coordinates' in dictionary and dictionary['coordinates']):
			for negative in negatives: 
				if negative in dictionary['text']:
					newPoint = {}
					print dictionary
					coords = dictionary['coordinates']['coordinates']
					newPoint['lat'] = float(coords[0])
					newPoint['lon'] = float(coords[1])
					newPoint['text'] = dictionary['text']
					newPoint['name'] = dictionary['user']['name']
					print newPoint
					entries.put(newPoint)
		return True

	def on_error(self, status):
		print status

class worker(Thread):
  def run(self):
  	while True:
  		output = plistlib.readPlist('points.plist')
  		while not entries.empty():
  			output.append(entries.get())
  		output = output[-300:]
  		plistlib.writePlist(output, 'points.plist')
  		print 'Wrote'
  		time.sleep(10)

class pusher(Thread):
	def run(self):
		while True:
			session = ftplib.FTP('neverderived.com','neverder','Echidna8801')
			f = open('points.plist','rb')                  # file to send
			session.storbinary('STOR /www/points.plist', f)     # send the file
			f.close()                                    # close file and FTP
			session.quit()
			print 'Pushed'
			time.sleep(20)

class waiter(Thread):
  def start(self):
  	twitterauth = OAuthHandler(twitterckey, twittercsecret)
  	twitterauth.set_access_token(twitteratoken, twitterasecret)
  	twitterStream = Stream(twitterauth, listener())
  	twitterStream.filter(track=keywords)

worker().start()
pusher().start()
waiter().start()