"""simulate the roulette wheel"""

num = int(input('Enter the number: '))

if num == 0:
    color = 'green'
elif num >= 1 and num <= 36:
    if (num >= 1 and num <= 10) or (num >= 19 and num <= 28):
        color = 'black' if num % 2 == 0 else 'red'
    else:
        color = 'red' if num % 2 == 0 else 'green'
else:
    color = False

print(f'You got in {color}.' if color else 'ERROR, OUT OF RANGE!')