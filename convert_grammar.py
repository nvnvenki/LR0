def getDictionary(grammar):

	grammar_dictionary = {}

	for eachProduction in grammar:
		production = eachProduction.split("->")
		if(grammar_dictionary.has_key(production[0])):
			grammar_dictionary[production[0]].append(production[1])
		else:
			grammar_dictionary[production[0]] = [production[1]]
	return grammar_dictionary

if __name__ == '__main__':
	g = ["E->E+T","E->T","T->T*F","T->F","F->(E)","F->i"]
	grammar = getDictionary(g)
	print grammar