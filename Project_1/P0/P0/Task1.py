"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

phonenum = set()

for text in texts:
    phonenum.add(text[0])
    phonenum.add(text[1])

for call in calls:
    phonenum.add(call[0])
    phonenum.add(call[1])

print(f'There are {len(phonenum)} different telephone numbers in the records.')
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
