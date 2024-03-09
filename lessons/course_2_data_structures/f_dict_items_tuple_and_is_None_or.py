
string = input('Enter file:')

if len(string) < 1:
    try:
        handle = open('mbox-short.txt')
    except:
        handle = open('../../data/sample/mbox-short.txt')
else:
    handle = open(string)


# Figure out who has sent the greatest number of mail messages

history = dict()

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        sender = words[1]
        history[sender] = history.get(sender, 0) + 1


# Find the most prolific committer

name = None
count = None

# ( key, value ) <--- tuple --<<<
for key, value in history.items():
    if count is None or count < value:
        count = value
        name = key

print(name, count)
