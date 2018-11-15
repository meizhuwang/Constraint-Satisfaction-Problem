import sys

def main(argv=None):
    vars=[]
    premises = sys.argv[1:]
    for premise in premises:
        for literal in premise:
            if literal!="~" and literal!="&" and literal!="|" and literal!="(" and literal!=")" and literal!=" ":
                if literal not in vars:
                    vars.append(literal)
    print_truth_table(vars,premises)


def print_truth_table(vars,premises):
    rows=variablemix(vars)

    varvalues=[]
    premisevalues=[]
    conclusionvalues=[]
    for row in rows:
        varvalues=[]
        premisevalues=[]
        conclusionvalues=[]
        for variable in sorted(vars):
            varvalues.append(row[variable])
        for premise in premises:
            print("premise",premise)
            print("evaluatepremise(premise,row)",evaluatepremise(premise,row))
            premisevalues.append(evaluatepremise(premise,row))
        if False not in premisevalues:
            print("variables",sorted(vars),varvalues,"premises",premises,premisevalues)


def variablemix(variables):
    if len(variables) == 0:
    	return [dict()]
    variables = list(variables)
    P = variables[0]
    R = variablemix(variables[1:])
    add_P = lambda v: [ dict([(P,v)] + list(r.items())) for r in R ]
    return add_P(True) + add_P(False)
# referencing truthtable

def evaluatepremise(premise,row):
    evalpremise=""
    for literal in premise:
        if literal == "~":
            value="not"
        elif (literal != "&") and (literal != "|") and (literal != "(") and (literal != ")") and (literal != " ") and (literal!="~"):
            value=str(row[literal])
        else:
            value=literal
        evalpremise=evalpremise+value

    return eval(evalpremise)

if __name__ == '__main__':
	sys.exit(main())
