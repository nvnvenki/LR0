import re
from read import read_grammar
class item:
	def __init__(self):
		self.sl = []
		self.name = " "
		self.fro = " "
		self.on = " "
		self.D = {}

	def setname(self,nu):
		self.name = str(nu)

	def setfron(self,fr,o):
		self.fro = fr
		self.on = o

	def __eq__(it):
		if self.sl == item.sl:
			return 1

		else:
			return 0

def findSym(it):
	l = []
	for st in it.sl:
		m = re.search(".*[.](.).*",st)
		if m:
			if m.group(1) not in l:
				l.append(m.group(1))

	return l

def shiftDot(st):
	m1 = re.search("(.*)[.](.)(.*)",st)
	tar = m1.group(1)+m1.group(2)+'.'+m1.group(3)
	return tar
	
def closure(a,temp,sym):

	temp_list = list()

	for st in a:
		m1 = re.match('(%s)->.*'%sym,st)
		if m1:
			temp.append(m1.group())
			temp_list.append(m1.group())
			
	for stri in temp:
		if stri in a:
			a.remove(stri) 
			#temp2 = []
			
	for s in temp_list:
		m1 = re.search('.*[.](.).*',s)
		if m1:
			ch = str(m1.group(1))
			if (ch!=sym) and (ch.isupper()):
				closure(a,temp,ch)

def createspace(string):
	temp = ""
	for s in string:
		c = s + ' '
		temp = temp+c

	return temp
	
#code begins now!!!!!
def getclosures(list_):
	#l = ["E->E+T","E->T","T->T*F","T->F","F->(E)","F->i"]
	l = []
	for i in range(len(list_)):
		list_[i] = list_[i].replace(" ","")

		
	for st in list_:
		#m1 = re.search("(.)->(.*)",st)
		#if not(m1.group(2) == 'eps'):
		l.append(st)
	
	'''
	for j in range(len(l)):
		m1 = re.search("(.)->(.*)",l[j])
		if m1.group(2) == 'eps':
			l.remove(m1.group())
	'''		

	
	m = re.search("(.)->.*",l[0])
	ns = 'H' + '->' +m.group(1)
	l.insert(0,ns)
	
	b = []
	for st in l:
		m = re.search("(.*)->(.*)",st)
		if m.group(2) == 'e':
			s = m.group(1) + '->' + m.group(2) + '.'
			b.append(s)
		else:
		
			s = m.group(1)+'->'+'.'+m.group(2)
			b.append(s)
	
	
	
	a = []
	onemore = b[:]
	m = re.search(".*[.](.).*",b[0])
	closure(onemore,a,m.group(1))
	a.insert(0,b[0])
	#print a
	'''
	a = []
	for eachProd in c:
		m = re.search("(.*)->(.*)",eachProd)
		if m.group(2) != "e.":
			a.append(eachProd)
	'''
	#print a


#a = ["S->.E","E->.Ad","A->.ABg","B->.h"]
#a = ["S->.E","E->.L=R","E->.R","L->.*R","L->.i","R->.L"]
#a = ["S->.E","E->.lMH","M->.M+H","H->.i"]
#a = ["S->.E","E->.T","T->.G","T->.HG","T->.i","G->.e","H->.f"]
#a = ["S->.E","E->.E+T","E->.T","T->.T*F","T->.F","F->.(E)","F->.i"]
#a = ["S->.E","E->.CC","C->.gC","C->.d"]
#a = ["I->.A","A->.BCDE","A->.a","B->.x","B->.y","C->.z","D->.k","E->.m","E->.n"]

#print a == b

	fol = []
	i0 = item()
	i0.setname('0')
	fol.append(i0)

	for st in a:
		i0.sl.append(st)

	visited = []
	count = 0
	for curr_item in fol:
		#print curr_item.sl
		if curr_item.name in visited:
			continue

		else:
			visited.append(curr_item.name)
			symlist = findSym(curr_item)
			#print symlist
			for sym in symlist:
				#print "for"+sym
				ni = item()
				#ni.setfron(i0.name,sym)

				l1 = []
				for st in curr_item.sl:
					m1 = re.match('.*[.](.).*',st)
					if m1 and m1.group(1) == sym:
						l1.append(m1.group())
				#print l1

				l2 = []
				for st in l1:
					l2.append(shiftDot(st))

				#print l2

				for s in l2:
					ni.sl.append(s)
					tlist = []
					m1 = re.search("(.)->.*[.](.).*",s)
					if m1:
						ch1 = m1.group(1)
						#print ch1
						ch2 = m1.group(2)
						#print ch2
						if (ch2.isupper()):
							onemore = b[:]
							closure(onemore,tlist,ch2)
					for stri in tlist:
						ni.sl.append(stri)

				ni1 = item()

				for st in ni.sl:
					if st not in ni1.sl:
						ni1.sl.append(st)

				del(ni)

				ni1.setfron(curr_item.name,sym)

				flag = 1
				for kr in range(0,len(fol)):
					if fol[kr].sl==ni1.sl:
						flag = 0
						name = fol[kr].name[:]
						ni1.setname(name)
						break

				if flag == 1:
					count+=1
					ni1.setname(count)
		
				fol.append(ni1)


	'''
	for j in range(0,len(fol)):
		print fol[j].name + ': '+fol[j].fro + ','+fol[j].on
		print fol[j].sl
	'''



	lod = []

	for j in range(0,len(fol)):
		d = {}
		d['from'] = [fol[j].fro] 
		d['to'] = [fol[j].name]
		d['on'] = [fol[j].on]
		for k in fol[j].sl:
			m1 = re.search("(.)->(.*)",k)
			str1 = m1.group(1)[:]
			str2 = m1.group(2)[:]
			if str1 in d.keys():
				d[str1].append(createspace(str2))
			else:
				d[str1] = [createspace(str2)]

		lod.append(d)

	return lod

if __name__=='__main__':
	
	filename = raw_input('Enter the file name:\n')
	list_ = read_grammar(filename)
	fl = getclosures(list_)
	#print list_
	
	#a = ["S->.H","H->.aHbB","B->.aA","A->.b"]
	#fl = getclosures()
	
	for d in fl:
		print d	
	

