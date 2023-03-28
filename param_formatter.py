import os
import glob
import csv

dir_path = '/home/maary/Documents/code/python/params'

csv_files = glob.glob(os.path.join(dir_path, '*.csv'))

indent_str = " " * 8

for csv_file in csv_files:
    name = os.path.splitext(csv_file)[0]
    with open(csv_file) as f :
        reader = csv.reader(f)

        with open(os.path.join(dir_path, name), 'a+') as fo:
            for row in reader:
                fo.write("\n")
                if len(row) == 5:
                    fo.write("{}: {}, 默认：{} \n".format(row[0], row[1], row[2]))
                    fo.write(f"{indent_str}{row[4]}\n")
                    fo.write(f"{indent_str}{row[3]}\n")
                if len(row) == 1:
                    fo.write("**********\n")
                    fo.write("{}\n".format(row[0]))
                    fo.write("**********\n")

