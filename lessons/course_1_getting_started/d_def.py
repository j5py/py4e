
# Hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours

def compute_pay(h, r):
    if h <= 40:
        return h * r
    else:
        return 40 * r + ((h - 40) * (r * 1.5))


# Prompt the user for hours and rate

try:
    a = float(input('Enter Hours: '))
    b = float(input('Enter Rate: '))

    # Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)

    print('Pay', compute_pay(a, b))
except:
    print('Not a numeric value')
