import csv
import sys


def main():
    print(sys.argv)
    with open(sys.argv[1], newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',') #Changing to use cvs.DictReader
        rows = [r for r in reader]
        print(rows[0], rows[162])


if __name__ == '__main__':
    main()
