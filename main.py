from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/list_basic/'

if __name__ == '__main__':
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    # count = 1
    # for i in items:
    #     # .strip('\n') removes the extra line added from the item name
    #     itemName = i.find('h4', class_='card-title').text.strip('\n')
    #     itemPrice = i.find('h5').text
    #     print('%d) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    #     count += 1
    pages = soup.find('ul', class_='pagination')
    urls = ['?page=1']
    links = pages.find_all('a', class_='page-link')
    # Check if the code is getting the 'Next' page button and discard it to avoid duplicate pages
    for link in links:
        pageNum = int(link.text) if link.text.isdigit() else None
        if pageNum is not None:
            x = link.get('href')
            urls.append(x)
    print(urls)
    count = 1
    for i in urls:
        newUrl = url + i
        response = requests.get(newUrl)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for j in items:
            # .strip('\n') removes the extra line added from the item name
            itemName = j.find('h4', class_='card-title').text.strip('\n')
            itemPrice = j.find('h5').text
            print('%d) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
            count += 1
