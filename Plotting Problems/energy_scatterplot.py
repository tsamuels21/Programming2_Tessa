# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c

'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

header = data.pop(0)
print(header)

k_schools = [x[6] for x in data]

print(k_schools)

k = []
for x in range(len(k_schools)):
    if k_schools[x]  == "K-12 School":
        k.append(data[x])

print(k)

names = [x[2] for x in k]

ghg = []
square = []

for place in k:
    try:
        gas = float(place[20])
        feet = float(place[7])
        ghg.append(gas)
        square.append(feet)

    except:
        print("nope")


print(ghg)
print(square)

lh_ghg = [x for x in ghg]
lh_square = [x for x in square]

fwp = [x for x in k[names.index('Francis W Parker School')]]    # finds Lincoln Park data
print(fwp)

fwp_ghg = int(fwp[20])
fwp_feet = int(fwp[7])
print(fwp_ghg)
print(fwp_feet)

plt.figure(1)

plt.scatter(square, ghg, color='lightblue')

plt.scatter(fwp_feet, fwp_ghg, color='pink', label='Francis W. Parker')

plt.title("Gas Emissions -vs- Building Square Footage")
plt.xlabel("Square Feet")
plt.ylabel("Gas Emitted")

plt.legend()

plt.show()
