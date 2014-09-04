import ctags
from ctags import CTags, TagEntry
import sys

try:
	tagFile = CTags('tags')
except:
	sys.exit(1)

entry = TagEntry() 
# TAG_PARTIALMATCH - begin with
# TAG_FULLMATCH - full length matching
# TAG_IGNORECASE - disable binary search
# TAG_OBSERVECASE - case sensitive and allowed binary search to perform

if tagFile.find(entry, 'BeautifulSoup', ctags.TAG_PARTIALMATCH | ctags.TAG_IGNORECASE):
    print 'found'
    print entry['lineNumber']
    print entry['pattern']
    print entry['kind']

# Find the next tag matching the name and options supplied to the 
# most recent call to tagFile.find().  (replace the entry if found)
status = tagFile.findNext(entry)

# Step to the next tag in the file (replace entry if found)
status = tagFile.next(entry)
