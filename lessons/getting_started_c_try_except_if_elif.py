
# Prompt for a score between 0.0 and 1.0

try:
    score = float(input('Enter Score: '))

    if score >= 0.0 and score <= 1.0:

        # If the score is between 0.0 and 1.0, print a grade

        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score < 0.6:
            print('F')

    else:

        # If the score is out of range, print an error

        print('Not between 0.0 and 1.0')

except:
    print('Not a numeric value')
