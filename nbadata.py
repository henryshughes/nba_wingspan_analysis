import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://craftednba.com/player-traits/length'

driver = webdriver.Chrome()
driver.get(url)

page = driver.page_source

height_list_string = []
wingspan_list_string = []

height_list_int = []
wingspan_list_int = []

soup = BeautifulSoup(page, 'html.parser')

for employee_data in soup.find_all('tbody'):
   rows = employee_data.find_all('tr')
   
for row in rows:
    height = row.find_all('td')[3].text
    height_list_string.append(height)
    wingspan = row.find_all('td')[4].text
    wingspan_list_string.append(wingspan)

for i in range(len(height_list_string)):
      # Split the string into feet and inches components

    feet_str, inches_str = height_list_string[i].split("\'")

    # Convert the feet component to inches
    feet_inches = float(feet_str) * 12

    # Convert the inches component to a float
    inches = float(inches_str[:-1])

    # Add the feet and inches components together to get the total height in inches
    total_inches = feet_inches + inches
    total_feet = total_inches/12

    height_list_int.append(round(total_feet, 2))
    
for i in range(len(wingspan_list_string)):
      # Split the string into feet and inches components

    feet_str, inches_str = wingspan_list_string[i].split("\'")

    # Convert the feet component to inches
    feet_inches = float(feet_str) * 12

    # Convert the inches component to a float
    inches = float(inches_str[:-1])

    # Add the feet and inches components together to get the total height in inches
    total_inches = feet_inches + inches
    total_feet = total_inches/12

    wingspan_list_int.append(round(total_feet, 2))
    

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