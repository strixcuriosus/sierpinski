numGens = int(raw_input("how many generations? (enter an integer)"))
G1 = [0 , 1, 0]
rules = {7:0, 6:0, 5:0, 4:1, 3:0, 2:0, 1:1, 0:0}
G2 = []
output = ''
baselength = len(G1) + numGens * 2


def printout(myList):
	global baselength
	while len(myList) < baselength:
		myList.insert(0,0)
		myList.append(0)
	output = ''
	for i in range(0, baselength):
		if myList[i] == 0:
			output += ' '
		else:
			output += 'X'
	print output

def getnextgen(currentgen):
	global numGens, baselength
	newgen =[]
	for i in range(1, baselength - 1):
		minilist = currentgen[i-1:i+2]
		minilist.reverse()
		rule = 0
		for j in range(0,3):
			rule += (2**j)*minilist[j]

		newgen.append(rules[rule])
	newgen.insert(0,0)
	newgen.append(0)
	return newgen

for i in range(0,numGens):
	printout(G1)
	G1 = getnextgen(G1)
    
