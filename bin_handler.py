import sys

def handler(string):

    # Read the entire file as a single byte string
    with open(string, 'rb') as fh:
        content = fh.read()
    print("Print the full content of the binary file:")

    bin_string = content.decode('ISO-8859-1')
    print(bin_string.split(','))

if __name__ == "__main__":
    handler(sys.argv[1])
