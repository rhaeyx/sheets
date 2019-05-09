from pyautogui import *
import time

filename = 'data_google.txt'

with open(filename) as f:
    data = f.read().split('\n')

ready_data = []

for data in data:
    splitted_data = data.split(' ')
    ready_data.append(splitted_data)

# Typing Data

# EDIT THIS
base_coord = (275, 200)


# Model #
click(base_coord)

for data in ready_data:
    typewrite(data[-2])
    typewrite('\n')
print('Model Done')

# Oregon #
scroll(100000)
time.sleep(2)
click(base_coord)

typewrite('\t')
for data in ready_data:
    typewrite(data[-1])
    typewrite('\n\t')
print('Oregon Done')