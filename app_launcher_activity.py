import csv

def convert(csv_path):
    with open(csv_path, newline='') as csv_file:
        output = '<!-- {} --> \n<item \n component="ComponentInfo{{{}/{}/}}" \n drawable="" />'
        reader = csv.reader(csv_file)
        for row in reader:
            print(output.format(row[0], row[1], row[2]))
            # print(row)


if __name__ == "__main__":
    convert('/home/maary/Downloads/pkg-2022-08-04-18-08-34.csv')