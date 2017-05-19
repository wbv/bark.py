#!/usr/bin/python2

from random import randrange as r
from sys import argv

barks = ["BARK", "WOOF", "BORK", "BARK"]
numbarks = len(barks)

def paragraph():
	for sentence in range(0, r(3,6)):
		for words in range(0, r(3,14)):
			print barks[r(0,numbarks)],
		print barks[r(0,numbarks)] + ". ",
	print "\n"

if __name__ == "__main__":
	if len(argv) < 2:
		paragraph()
		paragraph()
		paragraph()
	else:
		numpars = int(argv[1])
		for i in range(0,numpars):
			paragraph()

	print "BARK BARK,"
	print " DOGGO"
