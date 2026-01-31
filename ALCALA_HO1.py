def word_Length_vs_Number_Average():
    name = input('Whatts your name? boyyyy!!! -> ')
    haba = len(name)
    box = []
    average = 0

    for i in range(1,haba+1,1):
        number = eval(input(f'Enter a number {i} : '))
        average += number
        box.append(number)
        total = average / haba
    print(box)
    print(f'The length of the word is {haba}')
    print(f'The average of the number is {total}')
    if haba == total:
        print(f'The length of the word "{name}" is equal to the average.')
    elif haba > total:
        print(f'The length of the word "{name}" is greater than the average.')
    else:
        print(f'The length of the word "{name}" is less than the average.')
        print('lala')

word_Length_vs_Number_Average()