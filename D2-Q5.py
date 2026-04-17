#Q5. WAP using variable to find the area and circumference of a circle whose radous is 12cm 
# value of pi = 3.142
# area od circle = pi * r * r
# circumference of a circle = 2 * pi * r

r = int(input('enter radius: '))

# calculate area of circle 
area_of_circle = 3.142 * r * r
print(f'the area of circle is "{area_of_circle}"')

#calculate the circumference of circle
circumference_of_circle = 2 * 3.142 * r
print(f'the circumference of circle is "{circumference_of_circle}"')