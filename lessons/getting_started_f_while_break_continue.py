
# Program that repeatedly prompts a user for integer numbers until the user enters 'done'

largest = None
smallest = None


while True:
    string = input('Enter a numeric value: ')
    if string == 'done':
        break

    # If the user enters anything other than a valid number catch it with
    # a try/except and put out an appropriate message and ignore the number

    try:
        integer = int(string)
    except:
        print('Invalid input')
        continue

    if largest is None or largest < integer:
        largest = integer
    if smallest is None or smallest > integer:
        smallest = integer



# Once "done" is entered, print out the largest and smallest of the numbers

    # Enter 7, 2, bob, 10, and 4 to match excepted output

print('Maximum is', largest)
print('Minimum is', smallest)
