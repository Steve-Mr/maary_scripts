#!/usr/bin/python
# -*-coding:utf-8 -*-
import csv
import sys
from pathlib import Path
import pandas
import datetime
import os

names_dict = {'杨童旭':'', '马雯雯':'', '杜玉冰':'', '刘首辉':'', '刘郑':'', '孟瑞':'', '陶红辉':'', '高宇恒':'',} 

def process(csv_path):

    with open(csv_path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name = row[2]
            if name == '姓名':
                continue
            row = row[3:]
            index = 1
            report = []
            for cell in row:
                if cell:
                    fields = cell.split("|")
                    fields.insert(0, index)
                    results = ['','','','','']
                    for r_index, field in enumerate(fields):
                        results[r_index] = field
                    index+=1
                    report.append(results)
            names_dict[name] = report

        with open((Path(csv_path).parent).joinpath("result.csv"), 'w', encoding='UTF8', newline='') as dest:
            writer = csv.writer(dest)
            
            today = datetime.datetime.now()
            intervel = datetime.timedelta(days = 5)
            first_day = (today - intervel).strftime("%Y.%m.%d")
            today = today.strftime("%Y.%m.%d")

            title = '任务总结 时间：{}-{}'.format(first_day, today)
            writer.writerow([title,'','','','',''])
            writer.writerow(['姓名','编号','任务','进度','预期完成时间','问题'])
            for key, values in names_dict.items():
                if names_dict[key]:
                    for index, value in enumerate(values):
                        if(index == 0):
                            value.insert(0, key)
                        else:
                            value.insert(0, '')
                        writer.writerow(value)
                else:
                    writer.writerow([key,'','','','',''])
        
        source_csv = pandas.read_csv((Path(csv_path).parent).joinpath("result.csv"))
        dest_xlsx = pandas.ExcelWriter((Path(csv_path).parent).joinpath("{}.xlsx".format(today)))
        source_csv.to_excel(dest_xlsx, index=False)
        dest_xlsx.save()

        if os.path.exists((Path(csv_path).parent).joinpath("result.csv")):
            os.remove((Path(csv_path).parent).joinpath("result.csv"))
        

if __name__ == "__main__":
    print(sys.argv)
    # process('/home/maary/Downloads/周报（220828）（收集结果）-周报（220828）（收集结果）(1).csv')
    process(sys.argv[1])
    print('finished')
