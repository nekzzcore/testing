import csv

def calculate_average(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        total = 0
        count = 0
        for row in reader:
            for i in range(3, 8):  # Test1 to Final
                total += float(row[i])
                count += 1
        average = total / (count - 1)  # bug: divide by count - 1 instead of count
    return average
