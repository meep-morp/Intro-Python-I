def sieve_of_Eratosthenes(n):
    # Keeping track of time to compare different sieves

    is_prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if(is_prime[p] == True):
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0] = False
    is_prime[1] = False

    for p in range(n + 1):
        if is_prime[p]:
            print(p)


print(sieve_of_Eratosthenes(23))

# kudos to this video for explaining it well: https://www.youtube.com/watch?v=qEy_ChuL2fc
# Really cool history there too!
