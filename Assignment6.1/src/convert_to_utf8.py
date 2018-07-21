import sys #allows for remembering extension file has that can be used by others

input_x = sys.argv[1] # First interaction with directories
output_x = sys.argv[2] # Second interaction with directories

def main():
    with open(input_x, 'rb') as a: #opening Avengers.csv
        avengers = a.read()

    avengers_decoded = avengers.decode('iso-8859-1') #decoding file
    avengers_encode = avengers_decoded.encode('utf8') # encoding file

    with open(output_x, 'wb') as b: #writing encoded file
        b.write(avengers_encode)


if __name__ == '__main__': #Telling program to run
    main()

