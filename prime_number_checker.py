def prime_checker(number):
    if number == 1:
        print("It's not a prime number.")
    else:
        current_num = 2
        is_prime = True
        while number >= current_num:
            if number % current_num == 0 and current_num != number:
                is_prime = False
                break
            else:
                current_num += 1
        if is_prime == False:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
        
n = int(input()) # Check this number
prime_checker(number=n)