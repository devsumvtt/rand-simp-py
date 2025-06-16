"""get either red blue yellow
and print the result of them mixed"""

color1 = input('Enter the first color: ').lower()
color2 = input('Enter the second color: ').lower()

# order in alphabetical order
if color2 < color1:
    temp = color1
    color1 = color2
    color2 = temp

mixedColor = color1 + ' + ' + color2

if mixedColor == 'blue + red':
    finalColor = 'purple'
elif mixedColor == 'blue + yellow':
    finalColor = 'green'
elif mixedColor == 'red + yellow':
    finalColor = 'orange'
else:
    finalColor = False

print(f'{color1} + {color2} = {finalColor}' if finalColor else 'ERROR UNKNOWN COLOR MIXED')