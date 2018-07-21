import csv
import sys


def main():
    print(sys.argv)

    with open(sys.argv[1], 'r', newline='') as csv_file: #Opening file
        reader = csv.DictReader(csv_file, delimiter=',')
        rows = [r for r in reader]

    header = rows[0] #Setting header as the top row
    fieldnames = []
    for name in header:
        new_name = name.lower()
        new_name = new_name.strip('\n').strip('?') #Removing \n at the end of any records or any "?"
        new_name = new_name.replace('/', '_').replace(' ', '_') #Replacing slashes and spaced with underscores
        fieldnames.append(new_name) #Appending the fieldnames with the cleaned up version

    records = [] #Creating dictionary similar to previous weeks
    for row in rows:
        dictionary = {}
        for field, value in zip(fieldnames, row.values()):
            dictionary[field] = value
        records.append(dictionary)

    with open(sys.argv[2], 'w+', newline='') as csvfile:
        w = csv.DictWriter(csvfile, fieldnames=fieldnames) #Writing file using DictWriter with the created dictionary
        w.writeheader()
        w.writerows(records)


if __name__ == '__main__':
    main()
