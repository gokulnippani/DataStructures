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

marketers = set()
for call in calls:
    marketers.add(call[0])
for call in calls:
    marketers.discard(call[1])

for text in texts:
    marketers.discard(text[0])
    marketers.discard(text[1])

sorted_marketers = sorted(marketers)

print(f"These numbers could be telemarketers:")

print('\n'.join(map(str, sorted_marketers)))


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

