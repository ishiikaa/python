'''Two friends Suresh and Ramesh have m red candies and n green candies respectively.
They want to arrange the candies in such a way that each row contains equal number of candies
and also each row should have only red candies or green candies.
Help them to arrange the candies in such a way that there are maximum number of candies in each row.'''
def arrange_number(a, b):

   if a>b:

       s=b

   else:

       s=a

   for i in range(1, s+1):

       if a%i==0 and b%i==0:

           result=i

   return result

 

m=int(input())

n=int(input())

print(arrange_number(m,n))