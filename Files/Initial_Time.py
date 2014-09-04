import datetime

with open('last_query.txt', 'w') as f:
	f.write(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z UTC"))