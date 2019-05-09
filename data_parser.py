
filename = 'data_google.txt'

with open(filename) as f:
    data = f.read().split('\n')

data_to_save = []

for data in data:
    splitted_data = data.split(' ')
    data_to_save.append(splitted_data)


