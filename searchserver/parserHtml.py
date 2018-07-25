from bs4 import BeautifulSoup


def parser(content):
    soup = BeautifulSoup(content, 'html.parser', from_encoding='GBK')
    data = soup.find('div', {'class': 'content'})
    #print(data)
    return str(data)
