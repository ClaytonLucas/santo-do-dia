from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)  # Inicializa o Swagger

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

@app.route("/")
def home():
    """
    Obtém o santo do dia atual.
    ---
    responses:
      200:
        description: Retorna o santo do dia com nome, imagem, história, reflexão e oração.
        schema:
          type: object
          properties:
            results:
              type: array
              items:
                type: object
                properties:
                  nome:
                    type: string
                  imagem:
                    type: string
                  historia:
                    type: string
                  reflexao:
                    type: string
                  oracao:
                    type: string
    """
    page = requests.get('https://www.a12.com/reze-no-santuario/santo-do-dia', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    saint_list = soup.find("div", class_="saints-list")
    santo = []
    
    if saint_list:
        for a in saint_list.find_all('a', href=True):
            page = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')

            saint_name = soup.find('h1', class_='feature__name').text
            saint_infos = soup.find('div', class_='wg-text').find_all('p')
            info = "".join(p.text + "\n\n" for p in saint_infos[:-4])
            reflexao = "".join(p.text + "\n\n" for p in saint_infos[-3])
            oracao = "".join(p.text + "\n\n" for p in saint_infos[-1])
            imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

            santo.append({
                'nome': saint_name,
                'imagem': imagem,
                'historia': info,
                'reflexao': reflexao,
                'oracao': oracao
            })
    else:
        saint_name = soup.find('h1', class_='feature__name').text
        saint_infos = soup.find('div', class_='wg-text').find_all('p')
        info = "".join(p.text + "\n\n" for p in saint_infos[:-4])
        reflexao = "".join(p.text + "\n\n" for p in saint_infos[-3])
        oracao = "".join(p.text + "\n\n" for p in saint_infos[-1])
        imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

        santo.append({
            'nome': saint_name,
            'imagem': imagem,
            'historia': info,
            'reflexao': reflexao,
            'oracao': oracao
        })
    
    return jsonify(results=santo)

@app.route("/dia=<int:dia>&mes=<int:mes>")
def date(dia, mes):
    """
    Obtém o santo celebrado no dia e mês escolhidos pelo usuário.
    ---
    parameters:
      - name: dia
        in: path
        type: integer
        required: true
        description: Dia do mês desejado.
      - name: mes
        in: path
        type: integer
        required: true
        description: Mês desejado.

    responses:
      200:
        description: Retorna o santo do dia e mês informados.
        schema:
          type: object
          properties:
            results:
              type: array
              items:
                type: object
                properties:
                  nome:
                    type: string
                  imagem:
                    type: string
                  historia:
                    type: string
                  reflexao:
                    type: string
                  oracao:
                    type: string
    """
    page = requests.get(f'https://www.a12.com/reze-no-santuario/santo-do-dia?day={dia}&month={mes}', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    saint_list = soup.find("div", class_="saints-list")
    santo = []

    if saint_list:
        for a in saint_list.find_all('a', href=True):
            page = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')

            saint_name = soup.find('h1', class_='feature__name').text
            saint_infos = soup.find('div', class_='wg-text').find_all('p')
            info = "".join(p.text + "\n\n" for p in saint_infos[:-4])
            reflexao = "".join(p.text + "\n\n" for p in saint_infos[-3])
            oracao = "".join(p.text + "\n\n" for p in saint_infos[-1])
            imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

            santo.append({
                'nome': saint_name,
                'imagem': imagem,
                'historia': info,
                'reflexao': reflexao,
                'oracao': oracao
            })
    else:
        saint_name = soup.find('h1', class_='feature__name').text
        saint_infos = soup.find('div', class_='wg-text').find_all('p')
        info = "".join(p.text + "\n\n" for p in saint_infos[:-4])
        reflexao = "".join(p.text + "\n\n" for p in saint_infos[-3])
        oracao = "".join(p.text + "\n\n" for p in saint_infos[-1])
        imagem = "https://www.a12.com" + soup.find("div", class_="feature").find(class_="feature__portrait")["src"]

        santo.append({
            'nome': saint_name,
            'imagem': imagem,
            'historia': info,
            'reflexao': reflexao,
            'oracao': oracao
        })
    
    return jsonify(results=santo)

if __name__ == "__main__":
    app.run(debug=True)
