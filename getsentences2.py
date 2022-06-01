#function to split into sentences
def getsentences(t):
	#characters to split on
	splitters = '.?!'
	#where we'll put the sentences
	ss = []
	i = 0
	#go character by character
	while i < len(t):
		#reset the current sentence
		s = ''
		#read until the end of the text or
		#end of a sentence
		while i < len(t) and \
			t[i] not in splitters:
				s = s + t[i]
				i += 1
		#if the text isn't over, the current
		#character is the splitter and should
		#be appended
		if i < len(t):
			s = s + t[i]
		#go on to the next character
		i += 1
		#add current sentence to list
		ss.append(s)
	return ss

#remove non-space breaks and trim spaces
def makespaces(t):
	#characters to convert
	breaks = '\n\t'
	#output of 1st convert
	r1 = ''
	i = 0
	#go through 1 by 1
	while i < len(t):
		#current char should be converted?
		if t[i] in breaks:
			r1 = r1 + ' '
		else:
			r1 = r1 + t[i]
		i += 1
	#eliminate space after another space
	r2 = r1[0]
	#start at second character
	i = 1
	#go through the whole thing
	while i < len(r1):
		#check for two spaces in a row
		if r1[i] == ' ' and \
			r2[len(r2)-1] == ' ':
				#skip if so
				i += 1
				continue
		#otherwise, append current char
		else:
			r2 = r2 + r1[i]
		i += 1
	return r2

#remove spaces at edges of strings
def trimspaces(t):
	#result list
	r1 = []
	#go through one by one
	for s in t:
		#if first char is a space
		if s[0] == ' ':
			s = s[1:]
		slast = len(s) - 1
		#if last char is a space
		if len(s) > 0 and s[slast] == ' ':
			s = s[:slast]
		r1.append(s)
	#prune empty sentences
	r2 = []
	#go through one by one
	for s in r1:
		#check if sentence is empty
		if len(s) > 0:
			r2.append(s)
	return r2
