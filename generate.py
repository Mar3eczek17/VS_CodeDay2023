"""
Create a CSV dataset with 3 columns: status, blankets_creek, rope_nill
1. Start by reading status.txt and remove duplicates
2. Remove whitespace, non-alphanumerical characters
3. Force parse each line to infer the status
4. Create the CSV by writing the values with the columns
"""
import csv

statuses = set()
initial_count = 0
values = []


def normalize(line):
    line = line.lower()
    # Remove whit spaces
    line = line.strip()
    line = ''.join(i for i in line if i.isalnum() or i.isspace())
    return line


with open('status.txt', 'r') as f:
    for line in f.readlines():
        line = normalize(line)
        initial_count += 1
        statuses.add(line)

print(f"Initial count: {initial_count}")
print(f"Unique statuses: {len(statuses)}")

for status in statuses:
    if  "trails are open" in status:
        values.append([status, 1, 1])
    elif "trails are closed" in status:
        values.append([status, 0, 0])
    elif "blankets creek is open" in status:
        if "rope mill is open" in status:
            values.append([status, 1, 1])
        elif "rope mill is closed" in status:
            values.append([status, 1, 0])
    elif "rope mill is open" in statuses:
        if "blankets creek is open" in status:
            values.append([status, 1, 1])
        elif "blankets creek is closed" in status:
            values.append([status, 0, 1])


with open('status.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['status', 'blankets_creek', 'rope_mill'])
    writer.writerows(values)

