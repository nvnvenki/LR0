import copy
from finalclosures import getclosures
from read import read_grammar
from follow import find_follow
#Following is the function for determining to which state we have to shift.
def shift(a,i,j,K,T):
    for t in T:
        if i in t['from']:
            if a in t['on']:

                if a.isupper():
                    if K[j][a]=='':
                        K[j][a]=t['to'][0]
                    elif K[j][a] == t['to'][0]:
                        pass
                    else:
                        K[j][a]=K[j][a]+t['to'][0]
                else:
                    if K[j][a]=='':
                        K[j][a]='s'+t['to'][0]

                    elif K[j][a] =='s'+t['to'][0]:
                        pass
                    else:
                        K[j][a]=K[j][a]+'s'+t['to'][0]
    return K

#Following is the function for determining to which state we have to reduce.
def reduce(u,r,i,K,grammar,follow):    
    i1=int(i)
    r1=r.split('.')
    r2=r1[0].replace(' ','')
    for g in grammar:
        if u == g[0] and r2==g[1]:
            for f1 in follow[u]:
                if K[i1][f1]=='':
                    K[i1][f1]='r'+str(grammar.index(g)+1)
                elif K[i1][f1]=='r'+str(grammar.index(g)+1):
                    pass
                else:
                    K[i1][f1]=K[i1][f1]+" "+'r'+ str(grammar. index(g)+1)
                    

            return K

def generate_table(grammar1):
    grammar_list = grammar1[:]
    O = getclosures(grammar1)
    grammar = []
    k=0
    for prod in grammar_list:
        prod = prod.split("->")
        grammar.append(prod)
        s=grammar[k][0].replace(' ','')
        t=grammar[k][1].replace(' ','')
        grammar[k][0]=s
        grammar[k][1]=t
        k=k+1

    follow=find_follow(grammar1)

    max=0
    for o in O:
        S=o['to']
        integer = int(S[0])
        if integer > max:
            max=integer
    #Creating a dictionary containing all the elements of the grammar
    di={}
    di['$']=''
    t=[]
    for g in grammar:
        di[g[0]]=''
        list_=list(g[1])
        for l in list_:
            di[l]=''
    L=[]

    di['e']=''
    di['']=''
    del di['e']
    del di['']

    #Creating a list of dictionaries.
    for i in range(0,max+1):
        L.append(copy.deepcopy(di))
    #Checks whether to shift, reduce or accept
    for o in O:
        i=o['to'][0]
        i1=int(i)
        R=o.items()
        for r in R:
            for r1 in r[1]:
                # Checking if dot is present in string. Because '.' is not present in 'from','to','on' and 'state'
                if '.' in r1:
                    pos_of_dot=r1.index('.')
                    #Checking if dot is present in the middle of the string. If in middle goto shift
                    if pos_of_dot < (len(r1)-2):
                        
                        L = shift(r1[pos_of_dot+2],i,i1,L,O)
                    # If dot is present at the end of the string, reduce.
                    elif pos_of_dot==len(r1)-2 :
                        if len(r1)==4:
                            
                            r2=r1.split('.')
                            r3=r2[0].split(' ')

                            if r3[0]==grammar[0][0] and r[0]=='H':
                                L[i1]['$']='accept'
                            else:
                                L = reduce(r[0],r1,i,L,grammar,follow)
                        else:
                            L = reduce(r[0],r1,i,L,grammar,follow)
    
    return L

if __name__ == '__main__':

    file_name = raw_input('Enter the file name: \n')
    grammar = read_grammar(file_name)
    print grammar
    generate_table(grammar)
