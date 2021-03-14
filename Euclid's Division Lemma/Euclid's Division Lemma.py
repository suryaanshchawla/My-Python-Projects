#for each pair of positive integers  a  and  b, we have found whole numbers q and  r, satisfying the relation:
# a = bq+r, 0 =< r < b

# Question: for any given pair of integers, find it's q and r.

Ls=input("Enter the integers")
for a, b in ls:
    Ans= str(a) +"="+ str((a/b)-a%b)+ str(a%b)
