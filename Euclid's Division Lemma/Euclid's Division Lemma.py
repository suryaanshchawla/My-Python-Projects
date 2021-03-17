#for each pair of positive integers  a  and  b, we have found whole numbers q and  r, satisfying the relation:
# a = bq+r, 0 =< r < b

# Question: for any given pair of integers, find it's q and r.

# Algorithm
# 1. Take 2 integers
# 2. See the higher integer.
# 3. Put the higher one before the '='.
# 4. then put the smaller after the '='.
# 5. If they are equal, say that the no. are it's H.C.F.
# 6. print(larger int = smaller int * some no. + the reaminder)
# 7. repeat step 6 until r=0
# 8. when r=0, the devisor is the H.C.F.

def EuclidsDivAlg():
	try:
		devident=int(input("Enter the first natural num: "))
		devisor=int(input("Enter the second natural num: "))
	except:
		print("Please enter a natural number")
		print("For example: 256")

	r = devident % devisor
	q = devident // devisor

	if devident<devisor:
		devident=devisor
		devisor=devident
	elif devident==devisor:
		print("Both integers are same, so both are the HCF or each other.")

	while r != 0:
		print(str(step)+"."+str(devident)+"="+str(devisor)+"*"str(devident//devisor)+"+"+str(devident%devisor))
		if r != 0:
			devisor=devident
			r=devisor
EuclidsDivAlg()
