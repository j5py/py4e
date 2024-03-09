
# Write a program that prompts for a file name

string = input('Enter file name: ') # ../../data/sample/words.txt


# Then opens that file and reads through the file

try:
    handle = open(string)
except:
    print('Nothing found under:', string)
    quit()


# And print the contents of the file in upper case

for line in handle:
    print(line.rstrip().upper())
