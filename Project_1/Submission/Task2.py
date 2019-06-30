"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

timespent = dict()

for call in calls:
    time_for_call = int(call[3])
    if call[0] in timespent:
        timespent[call[0]] = timespent[call[0]]+time_for_call
    else:
        timespent[call[0]] = time_for_call

    if call[1] in timespent:
        timespent[call[1]] = timespent[call[1]] + time_for_call
    else:
        timespent[call[1]] = time_for_call

max_calls = 0
phone_num = ''

for phone in timespent:
    if timespent[phone]>max_calls:
        max_calls = timespent[phone]
        phone_num = phone

print(f'{phone_num} spent the longest time, {max_calls} seconds, on the phone during September 2016.')
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

