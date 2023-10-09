not_again = input("enter any charachter (except  -1) to start: ")


def prime(x):
    y = True
    if x > 1:
        for i in range(2, x // 2):
            if x % i == 0:
                y = False
                break
    else:
        y = False

    return y


while not_again != 0:
    number = int(input("Enter the number to test: "))

    if prime(number) == True:
        if number % 2 == 0:
            print("prime and even ")

        else:
            print("prime and odd")

    else:
        if number % 2 == 0:
            print("Not prime and even ")

        else:
            print("Not prime and odd")
    not_again = input("enter any charachter (except  -1) to start: ")
