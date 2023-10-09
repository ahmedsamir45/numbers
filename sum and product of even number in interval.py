x = eval(input("enter x: "))
y = eval(input("enter y: "))

# even numbers
sum_even = 0
product_even = 1

for i in range(x, y + 2, 2):
    product_even = i * product_even
    sum_even = sum_even + i

# odd numbers
sum_odd = 0
product_odd = 1

for i in range(x, y + 1):
    if i % 2 != 0:
        product_odd = i * product_odd
        sum_odd = sum_odd + i


print(
    "sumation of the even numbers =",
    sum_even,
    "\n",
    "product of the even number =",
    product_even,
)

print(" ")

print(
    "sumation of the odd numbers =",
    sum_odd,
    "\n",
    "product of the odd number =",
    product_odd,
)
