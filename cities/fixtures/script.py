
import csv
from cities.models import City

with open('cities/cities.csv', newline='') as fp:
    reader = csv.reader(fp, delimiter='\t')
    header = next(reader)
    for row in reader:
        #print(row[1], row[2], row[3].replace(',',''))
        c = City(name=row[1], country_id=row[2], population=int(row[3].replace(',','')))
        c.save()