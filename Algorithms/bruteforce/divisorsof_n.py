def divisors(n_param):

    n = n_param
    divisors_list = []

    for num in range (1, n + 1):

        if n % num == 0:
            #num is divisor of n
            divisors_list.append(num)

    return divisors_list        