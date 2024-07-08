from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
@app.route("/")
def home():
    page = requests.get('https://www.a12.com/reze-no-santuario/santo-do-dia', headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')
    
    saint_list = soup.find("div", class_="saints-list")
    santo = []
    if saint_list:
       
        
        for a in saint_list.find_all('a', href=True):
            
            page = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')

            
            saint_name = soup.find('div', class_='feature__name').text
            saint_infos = soup.find('div', class_='wg-text').find_all('p')
            info = ""
            reflexao = ""
            oracao = ""
            imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

            for saint_info in saint_infos[:-4]:
                info = info + saint_info.text + "\n\n"
            
            for saint_info in saint_infos[-3]:
                reflexao = reflexao + saint_info.text + "\n\n"
            
            for saint_info in saint_infos[-1]:
                oracao = oracao + saint_info.text + "\n\n"
            
            santo.append({
                'nome': saint_name,
                'imagem': imagem,
                'historia': info,
                'reflexao': reflexao,
                'oracao': oracao
            })

        

    else:
        saint_name = soup.find('div', class_='feature__name').text
        saint_infos = soup.find('div', class_='wg-text').find_all('p')
        info = ""
        reflexao = ""
        oracao = ""
        imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

        for saint_info in saint_infos[:-4]:
            info = info + saint_info.text + "\n\n"

        for saint_info in saint_infos[-3]:
            reflexao = reflexao + saint_info.text + "\n\n"

        for saint_info in saint_infos[-1]:
            oracao = oracao + saint_info.text + "\n\n"

        santo.append({
            'nome': saint_name,
            'imagem': imagem,
            'historia': info,
            'reflexao': reflexao,
            'oracao': oracao
        })
    
    return jsonify(results = santo)

@app.route("/dia=<int:dia>&mes=<int:mes>")
def date(dia, mes):
    page = requests.get(f'https://www.a12.com/reze-no-santuario/santo-do-dia?day={dia}&month={mes}', headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')
    
    saint_list = soup.find("div", class_="saints-list")
    santo = []
    if saint_list:
        
        
        for a in saint_list.find_all('a', href=True):
            
            page = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')

            
            saint_name = soup.find('div', class_='feature__name').text
            saint_infos = soup.find('div', class_='wg-text').find_all('p')
            info = ""
            reflexao = ""
            oracao = ""
            imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

            for saint_info in saint_infos[:-4]:
                info = info + saint_info.text + "\n\n"
            
            for saint_info in saint_infos[-3]:
                reflexao = reflexao + saint_info.text + "\n\n"
            
            for saint_info in saint_infos[-1]:
                oracao = oracao + saint_info.text + "\n\n"
            
            santo.append({
                'nome': saint_name,
                'imagem': imagem,
                'historia': info,
                'reflexao': reflexao,
                'oracao': oracao
            })

        

    else:
        saint_name = soup.find('div', class_='feature__name').text
        saint_infos = soup.find('div', class_='wg-text').find_all('p')
        info = ""
        reflexao = ""
        oracao = ""
        imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

        for saint_info in saint_infos[:-4]:
            info = info + saint_info.text + "\n\n"

        for saint_info in saint_infos[-3]:
            reflexao = reflexao + saint_info.text + "\n\n"

        for saint_info in saint_infos[-1]:
            oracao = oracao + saint_info.text + "\n\n"

        santo.append({
            'nome': saint_name,
            'imagem': imagem,
            'historia': info,
            'reflexao': reflexao,
            'oracao': oracao
        })
    return jsonify(results = santo)

if __name__ == "__main__":
    app.run(debug=True)



