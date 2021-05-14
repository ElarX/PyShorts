#two ways to do primes - one that keeps track of previously found primes, and a simple recursive approach with no memory
import numpy as np

#keep list of all known primes
knownPrimes = np.array([2])

def updatePrimes (number):
    '''
    :argument takes in a positive integer >1 and updates the stored list of primes
    :return null
    '''
    global knownPrimes

    #intelligently update the list of known primes
    for a in range (np.max(knownPrimes)+1, number+1):
        if 0 not in a%knownPrimes:
            knownPrimes = np.append(knownPrimes,a)


def isPrime(num):
    # define the ambiguity around 1
    if num == 1:
        return False

    updatePrimes(num)

    return num in knownPrimes


#recursiveSolution - no stored values

def isPrime2(num):
    if num ==1:
        return False #1 is not a prime number
    elif num==2:
        return True

    return False if primeHelper(num,num-1) ==0 else True

def primeHelper(target, curNum):

    #basecase
    if curNum ==1:
        return 1
    return target%curNum*primeHelper(target,curNum-1)



#one-line solution
def isPrime3(num):
    return False if np.prod(num%np.array(range(2,int(np.sqrt(num)+1)))) ==0 else True

#Try each of the options
print(f'is 5 prime? {isPrime(5)}')
print(f'is 10 prime? {isPrime2(10)}')
print(f'One line solution - is 9 prime? {isPrime3(9)}')
