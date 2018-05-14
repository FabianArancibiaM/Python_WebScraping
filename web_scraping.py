import urllib.request
import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range(1,6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content,'html.parser')
        "el div en que se encuentra la imagen"
        image_container = soup.find(id='comic')
        "el scr es la ruta de donde la obtienen"
        image_url = image_container.find('img')['src']
        "obtener ultimo elemento, nombre del archivo"
        image_name = image_url.split('/')[-1]
        print('Descargando imagen {}....'.format(image_name))

        urllib.request.urlretrieve('https:{}'.format(image_url),image_name)

if __name__=='__main__':
    run()