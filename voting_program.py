
import sys
import random 
from math import pow

a = random.randint(2, 10)
p=11
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
  
# Generating large random numbers
def gen_key(q):
  
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
  
    return key
# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
  
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
  
    return x % c

#
print("Welcome to the portal!\n")

#
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)# Private key for receiver



h = power(g, key, q)
publicKey= (q,g,h)
#

def youVoted(vote):
    if(vote==1):
        print("Your choice is : ABC")
    elif(vote==2):
        print("Your choice is : PQR")
    elif(vote==3):
        print("Your choice is : XYZ")
    else:
        sys.exit("You have entered an invalid number!")

voterID= int(input("Enter your Voter ID number(3 digit number): "))
#voter=(voterID,publicKey)
vote=int(input("You can vote for any one of these Candidates by entering the sl no. \n 1. ABC \n 2. PQR \n 3. XYZ \n Enter your choice : "))
youVoted(vote)

file = open("secretKey.txt",'a')
file.write(str(voterID)+" "+str(key)+"\n")
file.close()

sure=int(input("Do you want to change your vote? enter 1 for yes, 0 for no:  "))
if(sure==1):
    vote=int(input("You can vote for any one of these Candidates by entering the sl no. \n 1. ABC \n 2. PQR \n 3. XYZ \n Enter your choice : "))
    youVoted(vote)
finalVote=(publicKey,vote)

    
    
    
