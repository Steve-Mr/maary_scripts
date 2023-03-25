from datetime import datetime
from datetime import timedelta

def count_sec(x, y):
    fmt = '%H%M%S'
    num = 0

    x, y = datetime.strptime(x, fmt), datetime.strptime(y, fmt)
    while x != y:
        diff = set()
        hour = 9
        minute = int(x.strftime("%M"))
        sec = int(x.strftime("%S"))
        
        a = minute//10%10
        b = minute%10
        c = sec//10%10
        d = sec%10
        diff.add(a)
        diff.add(b)
        diff.add(c)
        diff.add(d)
        diff.add(9)
        if len(diff) == 5:
            num = num +1
            print(x,a,b,c,d)
        x = x + timedelta(seconds=1)
    print(num)

if __name__ == "__main__":
    count_sec('090000', '093000')
            

