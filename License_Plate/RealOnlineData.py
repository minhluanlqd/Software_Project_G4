#take data from an internet
import requests
from bs4 import BeautifulSoup
items=[]
license_plate=[]
# Collect and parse first page
page = requests.get('https://www.stolencar.com/Report/Search')
soup = BeautifulSoup(page.content, 'html.parser')
Car_stolen_list=soup.find_all(class_='col-sm-6')
for car in Car_stolen_list[1:]:
    c=car.get_text()
    items=c.split()
    if ((items[4]=='Plate:')):
        license_plate.append(items[5])
    elif (items[4]=='TEMPORARY'):
        pass        
    else:
        license_plate.append(items[4])
print (license_plate)
