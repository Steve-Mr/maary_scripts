import csv
import re
import sys
from pathlib import Path

def csv_writer(csv_path, rows):
    with open(csv_path, 'a+') as f:
        print('writing\n')
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

def get_raw():
    param_lines = []
    pattern = r'^(.*?)\((.*)default:(.*)\)\s*(.*)$'
    lines = [line for line in sys.stdin]
    raw = ' '.join(lines)
    raw_splitted = re.split(r'(?<=\S)~|~(?=\S)', raw.strip())
    for raw_param in raw_splitted:
        raw_param = raw_param.replace('\n', '')
        match = re.match(pattern, raw_param)
        if match:
            name = "~" + match.group(1).strip()
            type = match.group(2).strip()
            default = match.group(3).strip()
            desc = match.group(4).strip()
            param_lines.append([name, type, default, desc])
    print(param_lines)
    print(len(param_lines))
    return param_lines


if __name__ == '__main__':
    filename = input('filename: ')
    parent_path = Path(__file__).parent
    (parent_path / 'params').mkdir(parents=True, exist_ok=True)
    path = parent_path.joinpath("params/{}.csv".format(filename))
    print(path)
    csv_writer(path, get_raw())



