import os, sys, json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('updateNumber')
parser.add_argument('source')
args = parser.parse_args(["path", "1"])
if args.source:
	DATA_PATH = args.source
else:
	DATA_PATH = "/Users/john/Documents/SSB/Parsed Data"
	# DATA_PATH = "/home/jwvanderbeck/sc_parsed_data"

def test():
	print args.source
	print args.updateNumber

test()