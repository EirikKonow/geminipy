import sys
import os

"""
to run:
python3 idunnprog.py "name_of_file.kof" x
where x is min, med, or max.
"""

def makedict(filein: "File") -> {str: [[float, float, float], str]}:
	"""
	Sorts the gemini file's z-values unto a dictionary"
	
	Shape: dict[name] = [[z1, z2, z3], line]
	where z values are sorted from lowest to highest
	and line is the litteral file-line.
	"""
	
	myinfile = filein
	filedict = {}
	for line in myinfile:
		words = line.split()
		if len(words) > 0:
			if words[0] == "05":
				z = float(words[5])
				key = words[1]
				if not (key in filedict):
					filedict[key] = [z,0,0], line
				elif filedict[key][0][1] == 0:
					filedict[key][0][1] = z
				else:
					filedict[key][0][2] = z
					filedict[key][0].sort()
					
					
	return filedict
	
def makefile(filein: str, fileout: str, i: int) -> "Writes file":
	myinfile = open(filein, 'r+')
	myoutfile = open(fileout, 'w+')
	filedict = makedict(myinfile)
				
	print(len(filedict))
	
	for values in filedict:
		text = "%30s -> %s" % (str(filedict[values][0]), str(filedict[values][0][i]))
		#print(text)
		
		z = "%.3f" % (filedict[values][0][i])
		
		line1 = str(filedict[values][1])[:50]
		line2 = str(filedict[values][1])[57:]
		filetext = line1 + z + line2
		print(filetext)
		myoutfile.write(filetext)
	

	myinfile.close()
	myoutfile.close()
		
			
infilename = sys.argv[1]
# size_arg: str
size_arg = sys.argv[2]
size_select = {"min": 0, "med": 1, "max": 2}
# size: int
size = size_select[size_arg]
outfilename = infilename[:-4] + "_" + size_arg + ".kof"
makefile(infilename, outfilename, size)