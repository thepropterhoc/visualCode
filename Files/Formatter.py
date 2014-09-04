import plistlib

thePoints = []

with open('cleaned.txt', 'r') as f:
	for line in f.readlines():
		newPoint = {}
		lat = float(line.split(',')[0][1:])
		lon = float(line.split(',')[1][:-2])
		newPoint['lat'] = lat
		newPoint['lon'] = lon
		print newPoint
		thePoints.append(newPoint)

print thePoints

plistlib.writePlist(thePoints, 'points.plist')