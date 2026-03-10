from itertools import permutations

def smallest_prime_divisor(n):
    """Vrací nejmenší prvočíselný dělitel čísla n."""
    if n < 2:
        return None
    for i in [2, 3, 5, 7]:
        if n % i == 0:
            return i
    return n  # Pokud n je samo prvočíslo větší než 7

def find_numbers_with_two_prime_divisors():
    # Seznam pro uložení výsledků
    results = []

    # Projdeme všechny permutace devítimístného čísla z číslic 1 až 9
    all_numbers = permutations("123456789")

    for number_tuple in all_numbers:
        number = ''.join(number_tuple)
        
        # Najdeme nejmenší prvočíselné dělitele všech dvojmístných čísel
        divisors = set()
        for i in range(len(number) - 1):
            two_digit_num = int(number[i:i+2])
            divisor = smallest_prime_divisor(two_digit_num)
            if divisor is not None:
                divisors.add(divisor)
        
        # Pokud jsme našli právě dvě různá prvočísla jako dělitele
        if len(divisors) == 2:
            prime_pair = tuple(sorted(divisors))
            results.append((number, prime_pair))

    # Vypíšeme všechny dvojice prvočísel s odpovídajícími devítimístnými čísly
    for number, primes in results:
        print(f"Číslo: {number}, Prvočíselné dělitele: {primes}")

find_numbers_with_two_prime_divisors()
