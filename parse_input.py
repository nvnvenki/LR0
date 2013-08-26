import re
import generate_input
from read import read_grammar
from gen_table import generate_table

def parse_input(grammar_list,input_):

    grammar =  grammar_list[:]
    #table = generate_input.get_table()
    table = generate_table(grammar_list)
    return_value = []
    stack = ['0']
    symbols = ['$']
    if len(input_) == 0:
        return "Empty string"
    temp = []
    for i in input_:
        temp.append(i)
    #input_ = raw_input("enter input\n")
    input_ = temp
    input_.append("$")
    #print "-------------------------------------------------------------------------------------------------------------------------------------------"
    #print "STACK".ljust(40),"SYMBOLS".ljust(40),"INPUT".ljust(50),"ACTION".ljust(40)
    #print "-------------------------------------------------------------------------------------------------------------------------------------------"
    try:
        state = table[int(stack[len(stack)-1])][input_[0]]
        while state != "":
            current_line = {}
            current_line["stack"] = str(stack)
            current_line["symbols"] = str(symbols)
            current_line["input"] = str(input_)
            current_line["state"] = state
            if state.startswith('s'):
                #print str(stack).ljust(40),str(symbols).ljust(40),str(input_).ljust(50),state.ljust(40)
                stack.append(state[1:])
                symbols.append(input_.pop(0))
                state = table[int(stack[len(stack)-1])][input_[0]]
            elif state.startswith("r"):
                #print str(stack).ljust(40),str(symbols).ljust(40),str(input_).ljust(50),state.ljust(40)
                prev_state = state[:]
                length = len(grammar[int(prev_state[1:])-1].split("->")[1].strip().split(" "))
                check_eps = grammar[int(prev_state[1:])-1].split("->")[1].replace(" ","")
                if check_eps != "e":
                    for i in range(length):
                        stack.pop()
                next_state_num = table[int(stack[len(stack)-1])][grammar[int(prev_state[1:])-1].split("->")[0].strip()]
                stack.append(next_state_num)
                symbols = symbols[0:len(symbols)-length]
                next_symbol = grammar[int(prev_state[1:])-1][0]
                symbols.append(next_symbol)
                state = table[int(stack[len(stack)-1])][input_[0]]
            elif state.startswith("a"):
                #print str(stack).ljust(40),str(symbols).ljust(40),str(input_).ljust(50),state.ljust(40)
                state = table[int(stack[len(stack)-1])][input_[0]]
                #print "-------------------------------------------------------------------------------------------------------------------------------------------"
                #print "input accepted\n"
                break
            return_value.append(current_line)
        else:
            current_line = {}
            #print str(stack).ljust(40),str(symbols).ljust(40),str(input_).ljust(50),state.ljust(40)
            current_line["stack"] = str(stack)
            current_line["symbols"] = str(symbols)
            current_line["input"] = str(input_)
            current_line["state"] = "reject"
            #print "-------------------------------------------------------------------------------------------------------------------------------------------"
            #print "input rejected\n"
        return_value.append(current_line)
    except KeyError:
        #print "invalid symbol found in the input\nterminating the program..."
        return "Invalid symbol found"
    return return_value
if __name__ == "__main__":

    file_name = raw_input('Enter the file name: \n')
    grammar = read_grammar(file_name)
    input_ = raw_input("enter input\n").strip()
    x = parse_input(grammar,input_)
    print(x)






    