from threading import Thread
from pathlib import Path
import sys

index = 0
dest_array = ['end', 'start', 'mid']

def test(argv0, argv1):

    var1 = 'var'
    if(argv1 == 'test2'):
        var1 = 'var2'
    print(var1)
    print('0', argv0)
    print('1', argv1)
    print('=======')
    print(len(dest_array))
    global index
    print(index)
    ##index += 1
    print(index)
    print('----')
    print(index%len(dest_array))
    print('=====')
    while index < 6:
        print(index%len(dest_array))
        print('---')
        index+=1
    parent_path = Path(__file__).parent
    (parent_path / 'csvs').mkdir(parents=True, exist_ok=True)
    
    print('{}'.format(Path(__file__).with_name('script.sh')))

if __name__ == '__main__':
    test(sys.argv[1], sys.argv[2])