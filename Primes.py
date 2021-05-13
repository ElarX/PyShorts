#two ways to do primes - one that keeps track of previously found primes, and a simple recursive approach with no memory
import numpy as np

#keep list of all known primes
knownPrimes = np.array([2])

def updatePrimes (number):

    global knownPrimes

    #intelligently update the list of known primes
    for a in range (np.max(knownPrimes)+1, number+1):
        if 0 not in a%knownPrimes:
            knownPrimes = np.append(knownPrimes,a)


def isPrime(num):
    updatePrimes(num)

    #define the ambiguity around 1
    if num ==1:
        return True
    return num in knownPrimes


#recursiveSolution - no stored values

def isPrime2(num):
    if num ==1 or num==2:
        return True

    return False if primeHelper(num,num-1) ==0 else True

def primeHelper(target, curNum):

    #basecase
    if curNum ==1:
        return 1
    return target%curNum*primeHelper(target,curNum-1)

print(isPrime2(10))