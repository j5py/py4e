
# When you find a line that starts with "From" parse the line using split()

string = input('Enter file name: ')
if len(string) < 1:
    string = '../../data/sample/mbox-short.txt'


handle = open(string)
count = 0

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':


        # Print out the second word in the line

        print(words[1])
        count = count + 1


# Then print out a count at the end

print('There were', count, 'lines in the file with "From" as the first word')
