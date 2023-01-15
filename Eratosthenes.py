class Solution:
    def SieveOfEratosthenes(self):
        
        def primes_sieve(k):
            if k <= 2:
                return []
            primes = [1] * k
            primes[0] = 0
            primes[1] = 0
            
            for i in range(2, isqrt(k)+1):
                if primes[i]:
                    for j in range(i**2, k, i):
                        primes[j] = 0
            
            return [i for i in range(k) if primes[i]]