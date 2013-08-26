def read_grammar(file_name):


  #each production is a key value pair 
  grammar_dictionary={}
  fp = open(file_name,'r')

  grammar_productions_list =[]

  #reading eachLine in the file
  for eachLine in fp:

    grammar_productions_list.append(eachLine.strip())

  
  return grammar_productions_list



if __name__ == '__main__':

  user_input = raw_input('Enter the file name: \n')
  output =read_grammar(user_input)
  print output

