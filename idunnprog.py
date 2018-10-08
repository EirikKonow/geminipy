import sys
import os

def makefile(filein, fileout):
	myinfile = open(filein, 'r+')
	myoutfile = open(fileout, 'w+')
	filelist = []
	filedict = {}
	for line in myinfile:
		words = line.split()
		if len(words) > 0:
			if words[0] == "05":
				z = float(words[5])
				key = words[1]
				print("\n#############################")
				print("checking %s for %f" % (key, z))
				if key in filedict:
					print("Key found, old value: %f" % (filedict[key][0]))
					if float(filedict[key][0]) > z:
						print("New value determined lower, new value: %f" % z)
						filedict[key] = z, line
					else:
						print("New value determined higher, not setting new value: %f" % z)
				else:
					print("Key not found, generating key")
					filedict[key] = z, line
				print("#############################\n")
				filelist.append(words)
				
	print(len(filedict))
	
	for values in filedict:
		print(filedict[values][1])
		myoutfile.write(str(filedict[values][1]))
		#myoutfile.write("\n")
	

	myinfile.close()
	myoutfile.close()
		
			
infilename = sys.argv[1]
outfilename = infilename[:-4] + "_lowest_points.kof"
makefile(sys.argv[1], outfilename)