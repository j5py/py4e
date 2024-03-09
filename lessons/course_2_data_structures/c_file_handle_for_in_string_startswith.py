
# Write a program that prompts for a file name

string = input('Enter file name: ') # ../../data/sample/mbox-short.txt


# Then opens that file and reads through the file

handle = open(string)

iterations = 0
accumulation = 0

for line in handle:


    # Looking for lines of the form ---> X-DSPAM-Confidence:    0.8475

    if not line.startswith('X-DSPAM-Confidence:'):
        continue


    # Extract the floating point values from each of the lines and compute the average of those values

        # Do not use the sum() function or a variable named sum in your solution

    accumulation = accumulation + float(line[ line.find(':')+1 : ].strip())
    iterations = iterations + 1


print('Average spam confidence:', accumulation / iterations)
