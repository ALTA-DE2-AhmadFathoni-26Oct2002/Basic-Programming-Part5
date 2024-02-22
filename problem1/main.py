def prime_number(x):
    if x <= 1:
        return False
    elif x <= 3 :
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    elif x <= 5 :
        return True
    else:
        for i in range(5, 9):
            if x % i == 0:
                return False
            return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
    print(prime_number(10000000025))