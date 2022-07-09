#!/usr/bin/env python3

# This is a quick helper script that compiles the CSVs's of flavor names and descriptions and appends them to the _config.yml file
names_f = open("flavor-names.csv", "r")
descr_f = open("flavor-descriptions.csv", "r")

names = [n.strip() for n in names_f.readlines() if n.strip() != ""]
descr = [d.strip() for d in descr_f.readlines() if d.strip() != ""]

if len(names) != len(descr):
    print("files need to be the same length.")
    exit(-1)

output = "menu:\n"
for i in range(min(len(names), len(descr))):
    n, d = names[i], descr[i]
    n = n.replace('"', "'")
    d = d.replace('"', "'")
    output += f"  - name: \"{n}\"\n"
    output += f"    description: \"{d}\"\n"
print(output)
    



