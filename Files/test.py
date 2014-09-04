class tester(object):
	def __init__(self):
		self.writer = open('data.txt', 'w')
	def run(self):
		self.writer.write('hello')
		self.writer.write('fool')