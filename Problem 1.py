num=int(input("Entre a integer number:"))
if num > 1:


    for i in range(2, (num // 2) + 1):

    
        if (num % i) == 0:
            print(num, "is not a prime number")

    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
