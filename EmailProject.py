#!/usr/bin/python
import re
import sys


#def main(argv): 
	#dateRE = re.compile("^Date: .*")
	#subjectRE = re.compile("^Subject: .*")
	#fromRE = re.compile("^From: .*")
	#toRE = re.compile("^To: .*")
	#origMessageRE = re.compile("-----Original Message-----")
	#emailAddressRE = re.compile("<[^@]+@[^@]+\.[^@]+>")    
	#for line in sys.stdin: 
		#if (fromRE.match(line)):
			#if (emailAddressRE.search(line)):
				#addy = emailAddressRE.search(line).group(0)
				#if (len(addy) < 50):
					#print "LongValueSum:" + addy.lower() + "\t" + "1"
#if __name__ == "__main__": 
    #main(sys.argv) 


def main(argv): 
	dateRE = re.compile("^Date: .*")
	subjectRE = re.compile("^Subject: .*")
	fromRE = re.compile("^From: .*")
	toRE = re.compile("^To: .*")
	origMessageRE = re.compile("-----Original Message-----")
	emailAddressRE = re.compile("<[^@]+@[^@]+\.[^@]+>")    
	while True:
		s = sys.stdin.readline()
		if not s:
			break
		if (fromRE.match(s)):
			if (emailAddressRE.search(s)):
				addy = emailAddressRE.search(s).group(0)
				if (len(addy) < 50):
					print "LongValueSum:" + addy.lower() + "\t" + "1"
if __name__ == "__main__": 
    main(sys.argv) 
