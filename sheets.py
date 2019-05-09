from pyautogui import *

filename = 'data_google.txt'

with open(filename) as f:
    data = f.read().split('\n')

ready_data = []

for data in data:
    splitted_data = data.split(' ')
    ready_data.append(splitted_data)

print(ready_data) 

# Typing Data

base_coord = (300, 215)

# Model #
click(base_coord)

for data in ready_data:
    typewrite(data[1])
    typewrite('\n')
print('Model Done')

# Oregon #
scroll(100000)
click(base_coord)

typewrite('\t')
for data in ready_data:
    typewrite(data[2])
    typewrite('\n\t')
print('Oregon Done')