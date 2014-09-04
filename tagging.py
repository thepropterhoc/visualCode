import ctags, sys
from ctags import CTags, TagEntry
import pygraphviz as pgv

try:
	tagFile = CTags('tags')
except:
	sys.exit(1)

entry = TagEntry() 

patterns = {}
files = {}
# TAG_PARTIALMATCH - begin with
# TAG_FULLMATCH - full length matching
# TAG_IGNORECASE - disable binary search
# TAG_OBSERVECASE - case sensitive and allowed binary search to perform

# Find the next tag matching the name and options supplied to the 
# most recent call to tagFile.find().  (replace the entry if found)
status = tagFile.next(entry)
while status:
	fileName, pattern = entry['file'], entry['name']
	if fileName not in files:
		files[fileName] = [pattern]
	else:
		files[fileName] += [pattern]
	if pattern not in patterns:
		patterns[pattern] = [fileName]
	else:
		patterns[pattern] += [fileName]
	status = tagFile.next(entry)



patternGraph = pgv.AGraph()

for pattern in patterns.keys():
	for fileName in patterns[pattern]:
		patternGraph.add_edge(pattern, fileName)

patternGraph.layout()
patternGraph.draw('output.png')