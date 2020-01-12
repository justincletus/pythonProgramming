def prime(n):
    if n > 1:
        for i in range(2, n//2):
            if (n%i == 0):
                print("Number not a prime number")
                break
        else:
            print("number is prime number", n)
    else:
        print("number is not prime number", n)


prime(8)
