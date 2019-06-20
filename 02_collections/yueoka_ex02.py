# -*- coding: utf-8 -*-
def plus(x1,x2):
	return x1+x2
name_list=("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")

#x=range(len(name_list))

def name(names):
	for i,x in enumerate(names):
		if x == "Angy":
			print("{0}.My name is {1}".format(i,x))
		else:
			print("{0}.{1}is my classmate".format(i,x))



if __name__ == "__main__":
	a=1
	b=3
	print(plus(a,b))
	name(name_list)
	

