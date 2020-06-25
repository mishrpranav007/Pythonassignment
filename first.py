
import requests
from bs4 import BeautifulSoup
import csv
import time


def functionparse(response):
    print('HTTP GET: %s | Status code: %s' % (response.url, response.status_code))
    
    
    content = BeautifulSoup(response.text, 'lxml')
    
    findingtitles = [title.text for title in content.findAll('td', {'class': 'title'})]
    findinglinks = [link['href'] for link in content.findAll('a', {'class': 'no-js'})]
    findingdescriptions = [desc.text.strip() for desc in content.findAll('main', {'class': 'wrapper'})]
    findingimages = [link['href'] for link in content.findAll('a', {'class': 'no-js'})]
    
    findingnext_page = content.find('a', {'class': 'no-js'})['href']
    
    for findindex in range(0, len(findingtitles) - 1):
       results.append({
            'title': findingtitles[findindex],
            'link': findinglinks[findindex],
            'description': findingdescriptions[findindex],
            'images': findingimages[findindex]
            
        })
    
    
    urls.append(next_page)


def export_csv(filename):
    
    with open(filename, 'w') as csv_file:
        
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        
       
        writer.writeheader()
        
        
        for row in results:
           
            writer.writerow(row)
            


findpagenumber = 10
urls = []
results = []


html = requests.get('https://news.ycombinator.com/')
functionparse(html)

for pagenum in range(0, findpagenumber):
   
    findingnext_page = requests.get(urls[-1])
    parse(findingnext_page)
    time.sleep(2)

export_csv('newsfile.csv')
