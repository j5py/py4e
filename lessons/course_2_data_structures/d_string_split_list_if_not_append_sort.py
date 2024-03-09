
# The program should build a list of words

string = input("Enter file name: ") # ../../data/sample/romeo.txt
handle = open(string)
uniques = list()


# Split each line into a list of words using the split() method

for line in handle:
    words = line.split()
    for word in words:


        # Check to see if the word is already in the list and if not append it to the list

        if word not in uniques:
            uniques.append(word)


# When the program completes, sort and print

uniques.sort()
print(uniques)
