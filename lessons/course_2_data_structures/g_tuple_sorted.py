
# Figure out the distribution by hour of the day for each of the messages

string = input('Enter file:')

if len(string) < 1:
    try:
        handle = open('mbox-short.txt')
    except:
        handle = open('../../data/sample/mbox-short.txt')
else:
    handle = open(string)


# You can pull the hour out from the "From "" line by finding the
# time and then splitting the string a second time using a colon

# Example: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

distribution = dict()

for line in handle:
    parts = line.split()
    if len(parts) and parts[0] == 'From':
        for key in parts:
            if ':' in key:
                fragments = key.split(':')
                distribution[fragments[0]] = distribution.get(fragments[0], 0) + 1
                continue


# Once you have accumulated the counts for each hour, print out the counts, sorted by hour

# ( key, value )            <--- tuple --<<<
for key, value in sorted(distribution.items()):
    print(key, value)
