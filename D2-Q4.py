# Q4. WAP to input the Principal, Rate and Time and calculate the simple intrest
#simple intrest = (principal * rate * time)/ 100

principal = int(input('Enter the principal: '))
rate = int(input('Enter the rate: '))
time = int(input('Enter the time: '))

# calulate simple intrest
simple_intrest = (principal * rate * time)/ 100

print(f'the simple intrest is {simple_intrest}')