import csv
filename = "CSV_file.csv"
with open(filename,'r')as f:
    csv_reader= csv.reader(f)
    #iteator
    next(csv_reader)#for one row ahead
    for row in csv_reader:
        print(row)

