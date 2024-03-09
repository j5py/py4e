
count = 0
total = 0


while True:
    string = input('Enter a numeric value: ')
    if string == 'done':
        break
    try:
        comma = float(string)
    except:
        print(f'"{string}" is not a numeric value')
        continue
    count = count + 1
    total = total + comma


print('Count:', count)
print('Total:', total)
print('Average:', total / count)
