#Imports, including requests, matplotlib, beautifulsoup, and selenium
import requests
import math
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver

#Open the URL
url = 'https://craftednba.com/player-traits/length'

driver = webdriver.Chrome()
driver.get(url)

page = driver.page_source

#Create string lists for height and wingspan
height_list_string = []
wingspan_list_string = []
difference_list_string = []

#Parse the HTML content
soup = BeautifulSoup(page, 'html.parser')

#Create rows of table data
for employee_data in soup.find_all('tbody'):
   rows = employee_data.find_all('tr')
   
#Pull out the wingspan and height data
for row in rows:
    difference = row.find_all('td')[2].text
    difference_list_string.append(difference)
    height = row.find_all('td')[3].text
    height_list_string.append(height)
    wingspan = row.find_all('td')[4].text
    wingspan_list_string.append(wingspan)

#Function to convert the lists to floating point values from strings
def convert_list(input_list):
    output_list = []
    for i in range(len(input_list)):
      # Split the string into feet and inches components

        feet_str, inches_str = input_list[i].split("\'")

        # Convert the feet component to inches
        feet_inches = float(feet_str) * 12

        # Convert the inches component to a float
        inches = float(inches_str[:-1])

        # Add the feet and inches components together to get the total height in inches
        total_inches = feet_inches + inches
        total_feet = total_inches/12

        output_list.append(round(total_feet, 2))

    return output_list

def convert_to_integer(input_list):

    for i in range(len(input_list)):
        input_list[i] = float(input_list[i])

    return input_list

#Convert lists
height_list_int = convert_list(height_list_string)
wingspan_list_int = convert_list(wingspan_list_string)
difference_list_int = convert_to_integer(difference_list_string)


min_value = int(math.ceil(abs((min(difference_list_int)))) * math.copysign(1, (min(difference_list_int))))
max_value = int(math.ceil(abs((max(difference_list_int)))) * math.copysign(1, (max(difference_list_int))))

x_values = range(min_value, max_value)


def count_numbers_in_range(numbers_list, range_start, range_end, interval=1):
    count_list = []
    for i in range(range_start, range_end+1, interval):
        count = 0
        for j in numbers_list:
            if i <= j < i+interval:
                count += 1
        count_list.append(count)
    return count_list

grouped_heights = count_numbers_in_range(difference_list_int, min_value, max_value, 1)
del(grouped_heights[-1])

plt.title('Wingspan to Height Differential of NBA Players')
plt.xlabel('Inch Differential Relative to Height')
plt.ylabel('Number of Players')
plt.bar(x_values, grouped_heights)
plt.show()

'''
#Plot using matplotlib
plt.plot(height_list_int, wingspan_list_int, 'ko', markersize = 1)
plt.plot([5.8, 8], [5.8, 8], linewidth=2)
plt.plot([5.8, 8], [6.2, 8.4], linewidth=2)

location = 0 # For the best location
legend_drawn_flag = True
plt.legend(['NBA Player Data Points', 'Wingspan = Height',
             'Wingspan = Height + 5 Inches'], loc=0, frameon=legend_drawn_flag)

plt.xlabel('Height')
plt.ylabel('Wingspan')
plt.title('Wingspan vs Height')
plt.xlim(5.8, 8)
plt.ylim(5.8, 8)
plt.show()
'''