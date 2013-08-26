from read import read_grammar
import re

def find_first(grammar):
	
	#Algo for first
	# -> If X is a termianal , then First(X) = {X}
	# -> If X is a non terminal & X -> Y1 Y2 Y3....YK is a production for some k >= 1
	#	  then place a in First(X) if ro some i, a is in First(Yi) & eps is in all of First(Y1)....First(Yi)
	#      If eps is in First(Yj) for all j = 1,2,...k then add eps to First(X)
	# -> If X -> eps is a production tehn add eps to First(X)

	# First inialize the First dictionary
	first = {}
	# get the non terminals list first
	non_terminals_list = grammar.keys()
	#unnecessary 'start' key - remove it 
	#non_terminals_list.remove('start')
	#print non_terminals_list
	#for each non-terminal get the first list


	for non_terminal in non_terminals_list:
		# list of elements in first set
		first_list = get_first_list(non_terminal,grammar,first)
		first[non_terminal] = first_list
	#make unique
	for symbol in first:
		first_list = list(set(first[symbol]))
		first[symbol] = first_list

	checkForeps(grammar,first)

	return first

# this function is to get the first set of a non-terminal symbol
def get_first_list(non_terminal,grammar,first):
	#list of first elements
	
	first_list = []
	#for each rhs of the production for that non-terminal
	for production in grammar[non_terminal]:
		m = re.search("[A-Z]+",production) # get the posn of first Upper case letter - bcoz Uppercase letter corresponds to non-terminal symbol
		#if found
		if m:
			if m.start() > 0:
				
				first_list.append(production[0]) # add first terminal in the begining of the production to the first list.
			elif m.start() == 0:
				#print production
				temp = first_of_next_symbol(production,first,grammar) #if no terminal @ the begining then find the first of non-terminal which does not derives eps
				
				if temp:
					#temp = list(set(temp))
					
					first_list = first_list + temp # add it to the first list


		else:
			if production is not "e":
				first_list.append(production[0]) #if the production only contains terminals add first symbol

	#if eps is in grammar add it to first list	
	if "e" in grammar[non_terminal]:
			if "e" not in first_list:
				first_list.append("e") 
	
	return first_list

def first_of_next_symbol(production,first,grammar):

	#for each symbol in production
	first_list = []

	for symbol in production:
		if first.has_key(symbol):
			first_list = first_list + first[symbol]

		else:
			if symbol.isupper():
				first_list = first_list + get_first_list(symbol, grammar, first)
			else:
				return first_list
			

		if len(production) > 1:

			if "e" in grammar[symbol]:
				
				for i in range(first_list.count("e")):
					first_list.remove("e")
					
				if production.index(symbol) + 1 < len(production) and production[production.index(symbol)+1:][0].isupper():
					temp = get_first_list(production[production.index(symbol)+1:][0], grammar, first)

				
					first_list = first_list + temp
					

					if "e" in temp:
						continue
					else:
						return first_list
				elif production.index(symbol) + 1 < len(production) and production[production.index(symbol)+1:][0].islower():
					first_list.append(production[production.index(symbol)+1:][0])
					return first_list
			else:
				return first_list
	return first_list

def checkForeps(grammar,first):

	for non_terminal in grammar.keys():
		for eachProduction in grammar[non_terminal]:
			m = re.match("[A-Z]+",eachProduction)
			if m:
				if m.end() == len(eachProduction):
					eps_present = True
					for symbol in eachProduction:
						if 'e' not in first[symbol]:
							eps_present = False
							break
					if eps_present:
						if 'e' not in first[non_terminal]:
							first[non_terminal].append('e')
					else:
						if 'e' in first[non_terminal]:
							first[non_terminal].remove('e')

if __name__ == '__main__':

	file_name = raw_input('Enter the file name: \n')
	grammar = read_grammar(file_name)
	first = find_first(grammar)
	print first
