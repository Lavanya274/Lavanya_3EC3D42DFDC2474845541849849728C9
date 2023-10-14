## implement a recursive function to calculate the factorial of given number 

def fac(no):
  if no==0:
    return 1
  else:
    return no* fac(no-1)

number=int(input("Enter a value:"))
result=fac(number)

print("The factorial of {} is {}.".format(number,result))
