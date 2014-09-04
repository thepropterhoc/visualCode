import ctags
from ctags import CTags, TagEntry
import sys
import subprocess
import sqlite3

def run_ctags(fName):
	subprocess.call(['ctags', '--fields=afmikKlnsStz', fName])

def parse_ctags(tagFile):
	tf = CTags(tagFile)
	e = TagEntry()
	results = []
	s = tf.first(e)
	while s:
		eP = {'name': e['name'], 'file': e['file'], 'pattern': e['pattern'], 'lineNumber': e['lineNumber'], 'kind': e['kind'], 'fileScope': e['fileScope']}
		results.append(eP)
		s = tf.next(e)
	return sorted(results, cmp = lambda x, y: cmp(x['file'].lower(), y['file'].lower()) if x['file'] != y['file'] else cmp(x['lineNumber'], y['lineNumber']))

def count_lines(fName):
	return sum(1 for line in open(fName))

def get_code(fName, start, end):
	x = [s for s in open(fName)]
	return x[start:end]

def create_db(dbName):
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	c.execute('create table snips (name varchar(50), file varchar(50), start long, end long, kind varchar(50), code text)')
	conn.commit()
	conn.close()

def dump_in_db(dbName, results):
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	for r in results:
		values = (r['name'], r['file'], r['lineNumber'], r['end'], r['kind'], ''.join(get_code(r['file'], r['lineNumber']-1, r['end']-1)),)
		c.execute('insert into snips values (?,?,?,?,?,?)', values)
	conn.commit()
	conn.close()

def main():
	if(len(sys.argv) > 2):
		create_db(sys.argv[2])
		dbName = sys.argv[2]
	else:
		dbName = 'test.db'

	line_count = count_lines(sys.argv[1])
	run_ctags(sys.argv[1])
	results = parse_ctags('tags')
	l = len(results)
	for n, t in enumerate(results):
		results[n]['end'] = results[n+1]['lineNumber'] if n < l-1 else line_count+1

	dump_in_db(dbName, results)
	#for i in results:
		#print "%24s [%10s], %3d -- %3d (%2d)" % (i['name'], i['kind'], i['lineNumber'], i['end'], i['end']-i['lineNumber'],)

########
# MAIN #
########

if __name__ == '__main__':
	main()
