import bs4, requests

def getAmazonPrice(productUrl):
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    res = requests.get(productUrl, headers=header)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
print('The price is ' + price)
