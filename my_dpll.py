import sys

def main(argv=None):
	argv = sys.argv
	filename = argv[1]
	f = open(filename)
	fLines = f.readlines()
	l1 = fLines[0].split(' ')
	v = int(l1[2])
	clauses = []
	for line in fLines[1:]:
		clauses.append([int(i) for i in line.split(' ')[:-1]])
	if not dpll(clauses,{},v):
		print("this is not possible")

def dpll(clauses,assigned,v):
	print("clauses at the beginning of dpll")
	print(clauses)
	print("assigned")
	print(assigned)
	if not clauses:
		print("I'm done")
		print(assigned)
		return True
	if len(assigned)==v:
		if clauses:
			print("all assigned clauses left")
			print(clauses)
			return False

	unitclauses=findunits(clauses)
	print("unitclauses")
	print(unitclauses)
	if unitclauses:
		clauses=apply(clauses,unitclauses,v)
		assigned=updateassign(assigned,unitclauses)
	print("after unitclause apply clauses and assigned")
	print(clauses)
	print(assigned)
	pure=findonepure(clauses)
	print("pure",pure)
	if pure:
		tryliteral=pure
	else:
		print("need to split")
		print(clauses)
		if [] in clauses:
			return False
		tryliteral={abs(clauses[0][0]):clauses[0][0]>0}
	print("tryliteral")
	print(tryliteral)

	tryclauses=apply(clauses,tryliteral,v)
	tryassigned=updateassign(assigned,tryliteral)
	print("tryassigned",tryassigned)
	otherwiseclauses=otherwiseapply(clauses,tryliteral,v)
	otherwiseassigned=otherwiseassign(assigned,tryliteral)
	print("tryassigned and otherwiseassigned")
	print(tryassigned,otherwiseassigned)
	print("tryclauses and otherwiseclauses")
	print("tryclauses")
	print(tryclauses)
	print("otherwiseclauses")
	print(otherwiseclauses)

	return  dpll(tryclauses, tryassigned,v) or dpll(otherwiseclauses,otherwiseassigned,v)

def findunits(clauses):
	unitclauses={}
	for clause in clauses:
		if len(clause)==1:
			unitclauses[abs(clause[0])]=(clause[0]>0)
	return unitclauses

def apply(clauses,literaldict,v):
	eliminatelist=[]
	updatelist=[]
	for clause in clauses:
		for literal in clause:
			if abs(literal) in literaldict.keys():
				if literaldict[abs(literal)]==(literal>0):
					eliminatelist.append(clause)
				elif literaldict[abs(literal)]!=(literal>0):
					if literal not in updatelist:
						updatelist.append(literal)
	for eliminate in eliminatelist:
		if eliminate in clauses:
			clauses.remove(eliminate)
	for i in range(v):
		for clause in clauses:
			for literal in clause:
				if literal in updatelist:
					clause.remove(literal)

	return clauses

def otherwiseapply(clauses,literaldict,v):
	eliminatelist=[]
	updatelist=[]
	for clause in clauses:
		for literal in clause:
			if abs(literal) in literaldict.keys():
				if literaldict[abs(literal)]!=(literal>0):
					eliminatelist.append(clause)
				elif literaldict[abs(literal)]==(literal>0):
					if literal not in updatelist:
						updatelist.append(literal)
	for eliminate in eliminatelist:
		if eliminate in clauses:
			clauses.remove(eliminate)
	for i in range(v):
		for clause in clauses:
			for literal in clause:
				if literal in updatelist:
					clause.remove(literal)

	return clauses


def updateassign(assigned,tryliteral):
	print("tryliteral",tryliteral)
	for key in tryliteral:
		assigned[key]=tryliteral[key]
	print("assigned",assigned)
	return assigned

def otherwiseassign(assigned,tryliteral):
	for key in tryliteral:
		assigned[key]= not tryliteral[key]
	return assigned

def findonepure(clauses):
	findpure={}
	eliminatelist=[]
	for clause in clauses:
		for literal in clause:
			if abs(literal) not in findpure.keys():
				findpure[abs(literal)]=literal>0
			elif abs(literal) in findpure.keys() and findpure[abs(literal)]!=literal>0:
				if abs(literal) not in eliminatelist:
					eliminatelist.append(abs(literal))
	for eliminate in eliminatelist:
		del findpure[eliminate]
	for key in findpure:
		return {key:findpure[key]}

if __name__ == '__main__':
	sys.exit(main())
