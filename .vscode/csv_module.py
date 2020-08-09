import csv
with open('names.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    #print(cs_read)
    for cont in csv_file:
        print(cont)
