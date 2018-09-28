def karatsuba(num1, num2):

    if num1 < 10 or num2 < 10:
        return num1*num2

    n = len(str(num1))
    halfn = n/2

    a = num1 / (10**(halfn))
    b = num1 % (10**(halfn))
    c = num2 / (10 ** (halfn))
    d = num2 % (10 ** (halfn))

    #c, d= divmod(num2,10**(halfn))


    ac = karatsuba(a,c)
    bd = karatsuba(b,d)

    ad_bc = karatsuba(a+b, c+d) - ac - bd

    prod = ac*(10**(2*halfn)) + ad_bc*(10**halfn) + bd
    return prod

#num1 = 123456
#num2 = 100000
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627
prod = karatsuba(num1, num2)
print(prod)
