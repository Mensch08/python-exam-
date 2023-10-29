import csv

header = ["id","email","name"]
with open("new.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    












