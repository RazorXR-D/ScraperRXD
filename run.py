import requests
from bs4 import BeautifulSoup
import csv

keyword = input(str('Input Nama Barang = '))

url = 'https://www.tokopedia.com/search?navsource=home&ob=5&q={}&st=product&page='.format(keyword)
headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
for page in range(1, 10):
    req = requests.get(url+str(page),headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    items = soup.findAll('div', 'css-1g20a2m')

    for itloop in items :
        try : name = ''.join(itloop.find('div', 'css-18c4yhp', 'spnSRPProdName').text)
        except : name = ''
        try : harga = ''.join(itloop.find('div' ,'css-rhd610', 'spnSRPProdPrice').text)
        except : harga = ''
        try : ulasan = ''.join(itloop.find('span','css-u49rxo','iSRPProdTabReview').text)
        except : ulasan = ''
        try : lokasi = ''.join(itloop.find('span','css-4pwgpi','spnSRPProdTabShopLoc').text)
        except : lokasi = ''
        print(name,'|',harga,'|',ulasan,'|',lokasi)






















    
   #merapihkan biar enter hilang dan sebagainnya pakai di awal ''.join(().text.strip.split())
   #untuk membuat agar bagian yg none tidak ke display dengan cara : try : web = itloop.find('',{'':''})['href'].replace('https://','').replace('www.','').split('/')[0] split untuk menampilkan sebelum tanda / 