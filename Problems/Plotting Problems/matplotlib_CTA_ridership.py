# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s


#1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
#2  Plot bus usage for the same years as a second line on your graph. (5pts)
#3  Plot bus and rail usage together on a third line on your graph. (5pts)
#4  Add a title and label your axes. (5pts)
#5  Add a legend to show data represented by each of the three lines. (5pts)
#6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)

import matplotlib.pyplot as plt
import csv


plt.figure(1, tight_layout=True, figsize=(8, 6))

with open('CTA_-_Ridership_-_Annual_Boarding_Totals.csv') as f:
    reader = csv.reader(f)  # create a reader object from csv library
    data = list(reader)    # cast it as a list

header = data.pop(0)
year = [x[0] for x in data]
# Rail usage last 10 years
rail = [x[3] for x in data]
rail_ten = rail[-10:]

year_ten = year[-10:]

ten_year = [int(x) for x in year_ten]
ten_rail = [int(x) for x in rail_ten]

plt.plot(ten_year, ten_rail, color='pink', label="Rail")
plt.title("CTA Ridership By Year - Last 10 Years")
plt.xlabel("Year")
plt.ylabel("Ridership")

plt.xticks(ten_year, rotation=45, fontsize=8)


# Bus usage for same years
bus_usage = [x[1] for x in data]

bus = [x[1] for x in data]
bus_ten = bus[-10:]
ten_bus = [int(x) for x in bus_ten]

plt.plot(ten_year, ten_bus, color='lightblue', label="Bus")


# Plot both together on the same line (add them together)
total = [x[4] for x in data]
total_ten = total[-10:]
ten_total = [int(x) for x in total_ten]

plt.plot(ten_year, ten_total, color='thistle', label="Total")


plt.legend()

plt.show()

'''
Trends
After 2012 the total ridership of the CTA drops, with the bus riders dropping and the rail riders going slightly up, 
but then declining a bit in 2016. Also the rails seemed to be gaining more riders since 2008, but still less then bus.

# 1
One could be the growing popularity of ride share apps, like uber and lyft, with people taking ubers instead of the bus
or train to work or school.

# 2
Another reason could be people are fed up with the conditions of the CTA, or the wait times. It could be faster to walk 
or ride a bike then take the train and during rush hour it can take forever to get a train that isnt full of people. 


'''