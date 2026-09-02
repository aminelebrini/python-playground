N = input("enter the 1th number :")
N1 = input("enter the 2nd number : ")
product = 0
if((type(N) in (int, float)) and (type(N1) in (int, float))):

    product = N * N1

    if product > 0:
        print("is positiive !")
    elif product < 0:
        print("is negative !")
    else:
        print("is null !")
else: 
    print("check your inputs !")