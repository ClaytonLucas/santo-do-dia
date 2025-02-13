# Santo do Dia API

![Flask](https://img.shields.io/badge/Flask-1.1.2-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-WebScraping-green)
![Swagger](https://img.shields.io/badge/Swagger-API%20Docs-yellow)

Uma API simples desenvolvida com Flask que realiza web scraping para obter informações sobre o santo do dia a partir do site [A12](https://www.a12.com/reze-no-santuario/santo-do-dia). A API retorna detalhes como nome, imagem, história, reflexão e oração do santo do dia ou de uma data específica.

## 📌 Tecnologias Utilizadas

- **Python 3.x**
- **Flask** (Framework para APIs)
- **BeautifulSoup** (Para Web Scraping)
- **Requests** (Para requisições HTTP)
- **Flasgger** (Para documentação interativa com Swagger UI)

## 🚀 Instalação e Uso

### 1️⃣ Clonar o Repositório
```bash
 git clone https://github.com/ClaytonLucas/santo-do-dia-api.git
 cd santo-do-dia-api
```

### 2️⃣ Criar um Ambiente Virtual (Opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Projeto
```bash
python app.py
```

A API será executada em `http://127.0.0.1:5000/`.

## 📜 Rotas Disponíveis

### 🏠 Rota Principal - Santo do Dia

**Endpoint:**
```http
GET /
```

**Descrição:**
Retorna o santo do dia com nome, imagem, história, reflexão e oração.

**Exemplo de Resposta:**
```json
{
  "results": [
    {
      "nome": "São João Bosco",
      "imagem": "https://www.a12.com/caminho-para-imagem.jpg",
      "historia": "Descrição sobre a vida do santo...",
      "reflexao": "Uma reflexão sobre sua vida e ensinamentos...",
      "oracao": "Oração dedicada ao santo..."
    }
  ]
}
```

---

### 📅 Rota para Buscar Santo por Data

**Endpoint:**
```http
GET /dia=<int:dia>&mes=<int:mes>
```

**Parâmetros:**
- `dia` (int) → Dia do mês desejado.
- `mes` (int) → Mês desejado.

**Exemplo de Requisição:**
```http
GET /dia=31&mes=1
```

**Exemplo de Resposta:**
```json
{
  "results": [
    {
      "nome": "São João Bosco",
      "imagem": "https://www.a12.com/caminho-para-imagem.jpg",
      "historia": "Descrição sobre a vida do santo...",
      "reflexao": "Uma reflexão sobre sua vida e ensinamentos...",
      "oracao": "Oração dedicada ao santo..."
    }
  ]
}
```

## 📜 Documentação Interativa com Swagger
Após iniciar o servidor, acesse:
```http
http://127.0.0.1:5000/apidocs/
```
para visualizar e testar os endpoints diretamente pela interface interativa do Swagger.

## 📜 Observações
- O web scraping pode falhar caso o site de origem altere sua estrutura.
- Pode haver variação no tempo de resposta devido ao carregamento da página de origem.

## 📜 Licença
Este projeto está sob a licença MIT.

---

📌 **Desenvolvido por [Seu Nome](https://github.com/seuusuario)** ✨

