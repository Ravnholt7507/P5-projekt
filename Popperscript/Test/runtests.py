import os
import time
import pathlib
import sys

args = sys.argv
args.pop(0)

#--max-examples (default: 10000)
#--max-vars (default: 6)
#--max-body (default: 6)
#--max-literals (default: 40)
#allow_singletons. to your bias file.
#--eval-timeout (default: 0.001 seconds)
#--quiet (default: False)
#--debug (default: false)
#--stats (default: false)

file_path =  '/home/rune/Desktop/domainfiles/depots'
#file_path =  '/home/rune/Desktop/domainfiles/blocksworld'

poppercommand = "python3 popper.py -q"

outputfile = ">> output.txt"

strargs = " ".join(str(x) for x in args)

#with open('output.txt', 'w') as output:
#	output.truncate()

parent = pathlib.PurePath(file_path).name
print('Domain:', parent)

for foldername in os.listdir(file_path):

	start = time.time()

	f = os.path.join(file_path, foldername)
	if foldername ==".DS_Store":
		continue
	
	print('Action: ', foldername)

	with open('output.txt', 'a') as output:
		output.write(parent)
		output.write(',')
		output.write(foldername)
		output.write(',')
		output.write(strargs)
		output.write(',')
	
	os.system(poppercommand + " " + f +"/100 " + strargs + " " + outputfile)
	#os.system(poppercommand + " " + f + " " + outputfile)

	end = time.time()
	print('in:', round(end-start, 2))