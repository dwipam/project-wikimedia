import xml.etree.ElementTree as ET
import sys
import json

class word(object):
	def __init__(self, word, POS, priorProb, vandalism):
		self.word = word
		self.POS = POS
		self.priorProb = Prob
		self.vandalism = vandalism
		

def read_file(file):
	return(ET.parse(file))

def create_tree(data):
	text = []
	for i in data.iter('{http://www.mediawiki.org/xml/export-0.10/}text'):
		text.append(json.loads(i.text))
	return(text)
def give_proability(w1, w2, current_word):
	return 0

def main():
	data = read_file(sys.argv[1])
	data = create_tree(data)
	import pdb;pdb.set_trace()
if __name__=='__main__':main()
