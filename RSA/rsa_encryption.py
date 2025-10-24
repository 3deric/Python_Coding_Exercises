import math
import random
import time


def generate_keys():
    #generate list of primes
    primes = generate_primes(100)
    #randomize
    random.seed(time.time())
    #pick first prime
    i = random.randint(5, len(primes))
    j = i
    #pick second prime, must be larger then the first
    random.seed(time.time())
    j = random.randint(i + 1, len(primes))

    p = primes[i]
    q = primes[j]

    n = p * q
    phi_n = (p - 1) * (q - 1)

    
    for prime in primes:
        e = prime
        if math.gcd(phi_n, e) == 1:
            break
            
    d = pow(e, -1, phi_n)

    k_prv = (n, e)
    k_pub = (n, d)

    return (k_prv, k_pub)


def enc_msg(msg, k_priv) -> int:
    enc = msg ** k_priv[1] % k_priv[0] 
    return enc


def dec_msg(enc, k_pub) -> int:
    dec = enc ** k_pub[1] % k_pub[0]
    return dec


def generate_primes(target) -> int:
    primes = [2,3,5]
    number = 1

    while len(primes) < target:
        is_prime = False
        for prime in primes:
            if prime > math.sqrt(number):
                break
            if number%prime != 0:
                is_prime = True
            else: 
                is_prime = False
                break
        if is_prime == True and number >= 2 and number not in primes:
            primes.append(number)
        number+=1
    return primes


def main():
    keys = generate_keys()
    k_priv = keys[0]
    k_pub = keys[1]

    print(k_priv, k_pub) #show private and publc key

    value = 15
    print(f"Encrypting the value {value} with the private key {k_priv}.")

    crypt = enc_msg(value, k_priv) #encrypt with privatekey
    print(f"The encrypted value of {value} is {crypt}.")

    decrypt = dec_msg(crypt, k_pub) #decrypt with public key
    print(f"The decrypted value of {crypt} is {decrypt}.")


if __name__ == "__main__":
   main()
