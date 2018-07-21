import csv
import sys


def main():
    print(sys.argv)
    with open(sys.argv[1], newline='') as csv_file: #Per 14.1.1 opened with newline=''
        reader = csv.reader(csv_file, delimiter=',') #Returns a reader object which will iterate over lines in the cvsfile
        rows = [r for r in reader]
        print(rows[0], rows[162])


if __name__ == '__main__':
    main()
