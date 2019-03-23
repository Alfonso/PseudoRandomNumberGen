import sys
import subprocess as sp

#globals:
#Current value of RNG
X = 0
#Modulus exponent: M = 2^m
m = 0
#Multiplier
A = 0
#Increment
B = 0
#
M = 0

#helper function
def checkOptions(max):
    string = 'Enter your choice (1-'+str(max)+'): '
    user = int(input(string))

    tries = 1
    while((user<1) or (user>3)):
        if tries == 3:
            print('You have entered 3 invalid options. Goodbye!')
            sys.exit()
        print("Sorry, that is not a valid option")
        user = int(input(string))
        tries+=1
    return user

#seed
def seed_rnd(seed,algo):
    if algo == 1:
        m = 32
        A = 214013
        B = 2531011
    elif algo == 2:
        m = 32
        A = 1103515245
        B = 12345
    elif algo == 3:
        m = 31
        A = 1103515245
        B = 12345
    M = 2**m
    X = seed

def getRndMax():
    print(str(M))

def genRnd():
    X = (A * X + B) % M
    return X

def genRndLimit(limit):
    X = (A * X + B) % limit
    return X

def genRndRange(min,max):
    if min > max:
        return 0
    X = ((A * X + B) % (max - min) ) + min
    return X

def genRndFloat(min,max):
    print('')

def genRndExp(mean):
    print('')

#print the sequence of numbers generated
def printNums():
    print('')


print('1: Print RND_MAX\n2: 2: Generate uniformly-distributed positive integers\n3: Generate uniformly-distributed positive integers, up to a given limit\n4: Generate uniformly-distributed integers, from a given range\n5: Generate uniformly-distributed floats, from a given range\n6: Generate exponentially-distributed floats\n')

choice = checkOptions(6)

sp.call('cls',shell=True)

print('Select the algorithm to use.')

algo = checkOptions(3)

seed = int(input('Select the seed for the random number generator: '))
seed_rnd(seed,algo)

if choice == 1:
    #Print RND_MAX
    if algo == 1 or algo == 2:
        print('RND_MAX IS ',str(2**32))
    else:
         print('RND_MAX IS ',str(2**31))

elif choice == 2:
    num = int(input('How many numbers should I generate: '))
    #generate the numbers step 7
    #print the numbers
elif choice == 3:
    num = int(input('How many numbers should I generate: '))
    max = int(input('Enter the max number to generate'))
    #generate the numbers step 8
    #print the numbers
elif choice == 4:
    num = int(input('How many numbers should I generate: '))
    max = int(input('Enter the min number to generate'))
    min = int(input('Enter the max number to generate'))
    #generate the numbers step 9
    #print the numbers
elif choice == 5:
    num = int(input('How many numbers should I generate: '))
    max = int(input('Enter the min number to generate'))
    min = int(input('Enter the max number to generate'))
    #generate the numbers step 10
    #print the numbers
elif choice == 6:
    num = int(input('How many numbers should I generate: '))
    mean = int(input('Enter the mean of the distribution: '))
    if mean < 0:
        while(mean < 0):
            print("Error: the mean must be a positive number.")
            mean = int(input('Enter the mean of the distribution: '))
    #generate the numbers step 11
    #print the numbers
