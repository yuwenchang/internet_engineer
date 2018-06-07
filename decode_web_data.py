#encoding=utf8
from bs4 import  BeautifulSoup
import time
import re
import sys
from web_grap import web_grap
reload(sys)
sys.setdefaultencoding('utf8')

def decode_web_data(url):
    html = web_grap(url)
    soup = BeautifulSoup(html, 'html5lib', from_encoding='utf-8')
    lis = soup.findAll('li','item clearfix')
    for li in lis:
        title = li.findAll('p',class_= 'title')[0].getText().strip()
        href = li.findAll('p',class_= 'title')[0].findAll('a')[0].get('href')
        fid = re.search(r'\d{4,6}',href).group()
        big = li.findAll('span',class_='area-detail_big')[0].getText()+u'平米'
        price = li.findAll('div',class_='about-price')[0]
        total_price = price.findAll('p')[0].getText()
        every_price = price.findAll('p')[1].getText()
        print title +  "\t" + big
        print title + "\t" + "\t" + big + "\t" + total_price + "\t" + every_price

if __name__ == "__main__":
    decode_web_data("https://house.chizhouren.com/resoldhome/esf/list")
