values = [
	'0','1','2','3','4','5','6','7','8','9',
	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
	'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

URL_to_ID = {}
ID_to_URL = {}
index = 0
for i in values:
	for j in values:
		encodedID = '%s%s' % (i,j)
		URL_to_ID[encodedID] = index
		ID_to_URL[index] = encodedID
		index = index + 1

def urlToID(urlstring, version=0):
	try:
		return URL_to_ID[urlstring]
	except:
		return 0


def idToURL(idnum, version=0):
	if not idnum:
		idnum = -1

	print "Looking up ID %d" % idnum
	if idnum == -1:
		return '00'
	try:
		return ID_to_URL[idnum]
	except:
		return ''

