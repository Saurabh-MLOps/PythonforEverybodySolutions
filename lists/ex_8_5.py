lst = list()
while True:
    number = 0.0
    num = input('Enter number: ')
    if num =='done':
        break
    try:
       number = float(num)
    except ValueError:
       print('Enter a valid number')
       quit()

    lst.append(number)

print('Maximum:',max(lst) or None)
print('Minimum:',min(lst) or None)
