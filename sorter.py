import os
import sys

def sort(value = "min", file_name = None):
	#print(file)
	file = open("static/"+file_name, "r+")
	file_list = []
	for line in file:
		temp = line.split()
		if len(temp) != 0:
			if temp[0] == "05":
				file_list.append(line.split())

	name_dict = {}
	for i in file_list:
		for j in file_list:
			if i[1] == j[1]:
				if not j[1] in name_dict:
					name_dict[j[1]] = [j]
				else:
					if not len(name_dict[j[1]]) == 3:
						name_dict[j[1]].append(j)
	file.close()

	for key in name_dict:
		print(key)
		z0 = name_dict[key][0][5]
		z1 = name_dict[key][1][5]
		z2 = name_dict[key][2][5]

		if z0 >= z1 and z0 >= z2:
			name_dict[key][0].append("max")
		elif z1 >= z0 and z1 >= z2:
			name_dict[key][1].append("max")
		else:
			name_dict[key][2].append("max")

		if z0 <= z1 and z0 <= z2:
			name_dict[key][0].append("min")
		elif z1 <= z0 and z1 <= z2:
			name_dict[key][1].append("min")
		else:
			name_dict[key][2].append("min")

		for i in range(3):
			if "max" not in name_dict[key][i] and "min" not in name_dict[key][i]:
				name_dict[key][i].append("med")

	outfile = open("static/"+file_name+"_{}.kof".format(value), "w+", encoding="utf-8")
	for key in name_dict:
		for i in range(3):
			if value in name_dict[key][i]:
				number = name_dict[key][i][0]
				name = name_dict[key][i][1]
				id_num = name_dict[key][i][2]
				x_val = name_dict[key][i][3]
				y_val = name_dict[key][i][4]
				z_val = name_dict[key][i][5]

				#print(" %s %.19s %s %s %s %s" % ())

				#string = " {:3}{:11}{:10}{:14}{:11}{:11}\n".format(number, name, id_num, x_val, y_val, z_val)
				string = " {:3}{:11}{:10}{:14}{:11}{:11}\r\n".format(number, name, id_num, x_val, y_val, z_val)
				outfile.write(string)

if __name__=="__main__":
	# This repeats sorting all three 3 times, lol. It's fine though
	for i in ["min", "med", "max"]:
		sort(i, sys.argv[1])