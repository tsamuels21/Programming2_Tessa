import csv

with open('data/World firearms murders and ownership.tsv') as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

print(data)