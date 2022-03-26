import csv
data = []
with open("dwarf_stars.csv", "r") as f:
   csvreader = csv.reader(f)
   for row in csvreader:
      data.append(row)
headers = data[0]
planet_data = data[1:]
#Converting all planet names to lowercase
for data_point in planet_data:
  data_point[2] = data_point[2].lower()
#Sorting planet names in alphabetical order
planet_data.sort(key=lambda planet_data: planet_data[2])
with open("dataset_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

dataset_1 = []
dataset_2 = []
with open("dwarf_stars.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
   dataset_1.append(row)
with open("dataset_2_sorted.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
   dataset_2.append(row)
headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]
headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]
headers = headers_1 + headers_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
   planet_data.append(planet_data_1[index] + planet_data_2[index])
with open("final.csv", "a+") as f:
   csvwriter = csv.writer(f)
   csvwriter.writerow(headers)
   csvwriter.writerows(planet_data)    
