# number=0

# if number==0:
# 	print "Zero"
# elif (number%2)==0:
# 	print "Even"
# elif (number%2)==1:
# 	print "Odd"

# def timetable(arg):
# 	table=[]
# 	for j in xrange(1,11):
# 		table.append(str(arg)+"*"+str(j)+"="+str(arg*j))
# 	return table

# print timetable(2)
# print timetable(3)


def timetable(arg):
	table=[]
	for j in xrange(1,10):
		table.append(str(arg)+"*"+str(j)+"="+str(arg*j))
	return table

for j in range(2,6):
	for i in range(1,10):
		print timetable(j)[i-1]+"     "+timetable(j+4)[i-1]

def bubblesort(arg):
	for i in range(0, len(arg)-1):
		for j in range(0,len(arg)-1):
			if arg[j]>arg[j+1]:
				temp=arg[j]
				arg[j]=arg[j+1]
				arg[j+1]=temp

arg=[45,20,21,50,10,8,9,7,10]
bubblesort(arg)
print(arg)
