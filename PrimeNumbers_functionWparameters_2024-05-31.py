###Prime Numbers--functions with inputs##

# My code below this line 👇
divisors = []
def prime_checker(number):
    for i in range(1,101):
      if number % i == 0:
        divisors.append(i)
    if len(divisors) > 2:
      print("It's not a prime number.")
    else:
      print("It's a prime number.")

#My code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

##InstructorCode##
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)
##EndInstructorCode##