import json, requests

print requests.delete('http://54.213.159.144:4000/clear')

with open('coords.txt', 'r') as f:
	for line in f.readlines():
		deconstruct = tuple(line.strip().split(','))
		lat, lon = float(deconstruct[-2][2:]), float(deconstruct[-1][1:-2])
		text = ""
		for piece in deconstruct[:-2]:
			text = text + piece
		text = text[3:-1]
		print str(lat) + ', ' + str(lon) + ', ' + text
		data = {
		'text' : text, 
		'lat' : lat,
		'lon' : lon
		}
		
		print requests.post('http://54.213.159.144:4000/add',  headers={"content-type":"application/json"}, data=json.dumps(data))