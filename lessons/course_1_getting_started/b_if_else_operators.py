
# Prompt the user for hours and rate

h = float(input('Enter Hours: '))
r = float(input('Enter Rate: '))


# Hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours

if h <= 40:
    pay = h * r
else:
    pay = 40 * r + ((h - 40) * (r * 1.5))


# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)

print(pay)
