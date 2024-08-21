import csv
with open(r"C:\Users\himan\Desktop\sample.csv",'r') as F:
    reader=csv.reader(F)
    for row in reader:
        print(row)
F.close()