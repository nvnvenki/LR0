from read import read_grammar
from first import find_first



def find_follow(grammar):
  follow_not_found_dictionary ={}   
  grammar_dictionary = {}
  list_of_symbols_in_order = []

  for eachGrammarProduction in grammar:
     #removing extra spaces and new line character
     eachGrammarProduction = eachGrammarProduction.split("->")
     eachGrammarProduction[0] = eachGrammarProduction[0].replace(" ","")
     eachGrammarProduction[0] = eachGrammarProduction[0].replace("\n","")
     eachGrammarProduction[1] = eachGrammarProduction[1].replace(" ","")
     eachGrammarProduction[1] = eachGrammarProduction[1].replace("\n","")

     if not(eachGrammarProduction[0] in list_of_symbols_in_order):

      list_of_symbols_in_order.append(eachGrammarProduction[0])

     #if the same grammar has more than one production then add it to a list
     
     if(grammar_dictionary.has_key(eachGrammarProduction[0])):
       grammar_dictionary[eachGrammarProduction[0]].append(eachGrammarProduction[1])

     else:
       grammar_dictionary[eachGrammarProduction[0]] = [eachGrammarProduction[1]]

  follow_dictionary = {}
  first = find_first(grammar_dictionary)
  

  start_symbol = list_of_symbols_in_order[0]
  follow_dictionary[start_symbol] = ['$']

  for everySymbol in list_of_symbols_in_order[1:]:
      follow_dictionary[everySymbol] =[]

  for everySymbol in list_of_symbols_in_order:

      productions_found = find_productions(grammar_dictionary,everySymbol)
      process_productions_found(productions_found,first,follow_dictionary,follow_not_found_dictionary,everySymbol)


  for everySymbol in follow_not_found_dictionary.keys():
    if len(follow_not_found_dictionary[everySymbol]) != 0:
      for NonTerminal in follow_not_found_dictionary[everySymbol]:
        for eachTerminal in follow_dictionary[NonTerminal]:
          if eachTerminal not in follow_dictionary[everySymbol]:
            follow_dictionary[everySymbol].append(eachTerminal)


  return follow_dictionary


def find_productions(grammar , symbol):
    
    productions_found_dictionary = {}
    for eachKey in grammar.keys():
        temp_list = []
        for eachElement in grammar[eachKey]:
            
            if symbol in eachElement:
                temp_list.append(eachElement)

        productions_found_dictionary[eachKey] = temp_list

    for eachKey in productions_found_dictionary.keys():
      if len(productions_found_dictionary[eachKey]) == 0:
        del productions_found_dictionary[eachKey]

            
    return productions_found_dictionary  


def process_productions_found(productions,first,follow,follow_not_found_dictionary,symbol):
       
    follow_not_found_dictionary[symbol] = []

    for eachLeftHandSide in productions.keys():
       
       
       for eachRightHandSide in productions[eachLeftHandSide]:
         flag = 0
         i = -1 


         for everyCharacter in eachRightHandSide:
          if(flag == 0):
             i = i+ 1 
             if everyCharacter == symbol:
                 flag = 1
                 #examine the next character
                 #it should not be null
                 #if it is null then add the follow of left handside to the dictionary
                 #and also the left hand side should not be the same as "symbol"                
                 if((i+1) is len(eachRightHandSide)):

                     #if it is null then check the left hand side
                     #if it is same as the symbol for which follow is being found dont do anything
                     #else follow(leftHandSide) is follow(symbol)
                     #this is rule 3

                     

                     if not(eachLeftHandSide == eachRightHandSide[i]):
                         
                         if len(follow[eachLeftHandSide]) == 0:
                              #Follow of the symbol is not present
                              follow_not_found_dictionary[symbol].append(eachLeftHandSide)
                         else:
                               for everySymbol in follow[eachLeftHandSide]:
                                 if not(everySymbol in follow[symbol]):
                                  follow[symbol].append(everySymbol)


                     else:
                          if not ("$" in follow[symbol]):
                              follow[symbol].append("$")


                                          
                 else:
                     
                     temp_list = []
                     first_union_flag = 0
                     no_of_non_terminals_found_continuously = 0;
                     no_of_epsolon = 0
                     
                            
                     for s in range((i+1),len(eachRightHandSide)):
                         if not(eachRightHandSide[s].isupper()):
                            #This means that the follow of the symbol is first of beta 
                            #now it doesnt matter even if first of other non terminals contain eps
                            first_union_flag = 1
                            temp_list.append(eachRightHandSide[s])
                            no_of_non_terminals_found_continuously = 0;
                            no_of_epsolon = 0
                            break


                         else:
                              no_of_non_terminals_found_continuously =  no_of_non_terminals_found_continuously + 1
                              has_epsolon_flag = 0

                              for eachTerminal in first[eachRightHandSide[s]]:
                                  #e is epsolon
                                  if eachTerminal == "e":
                                      no_of_epsolon = no_of_epsolon +1
                                      has_epsolon_flag =1

                                  else:

                                      if not(eachTerminal in temp_list):
                                          temp_list.append(eachTerminal)

                              if has_epsolon_flag == 0:
                                break

                     if first_union_flag == 1:
                         for eachSymbol in temp_list:
                             follow[symbol].append(eachSymbol)

                     elif no_of_non_terminals_found_continuously == no_of_epsolon and not(no_of_non_terminals_found_continuously == 0):
                         for m in follow[eachLeftHandSide]:
                             if not(m in follow[symbol]):
                                 follow[symbol].append(m)

                         for a in temp_list:
                             if not(a in follow[symbol]):
                                 follow[symbol].append(a)

                              

                     elif no_of_non_terminals_found_continuously != no_of_epsolon:
                          for n in temp_list:
                              if not(n in follow[symbol]):
                                  follow[symbol].append(n)
                                  

             else:
                 continue

if __name__ == '__main__':
        
    file_name = raw_input('Enter File Name containing the grammar: \n')
    grammar = read_grammar(file_name)
    print find_follow(grammar)


