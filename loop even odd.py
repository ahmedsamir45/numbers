num =int(input("enter num to check even or odd. (enter -1 to end) "))
num_of_odd=0
num_of_even=0

while num!=-1:

    if num ==0 :
        print('0 is not even or odd')
    elif num %2==0 :
        print("even num")
        num_of_even+=1
    else:
        print('odd num')
        num_of_odd+=1

    num =int(input("enter num to check even or odd. (enter -1 to end) "))

print('the num of even: ',num_of_even)
print('the num of odd: ',num_of_odd)
