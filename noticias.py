import requests

# reemplaza YOUR_API_KEY con tu propia clave de API
api_key = "YOUR_API_KEY"

# URL base de la API de NewsAPI
url = "https://newsapi.org/v2/everything"

# parametros de la solicitud
params = {
    "apiKey": api_key,
    "q": "Atletico Nacional",
    "sources": "goal,winsports,espn,el-colombiano"
}

# realiza la solicitud GET a la API de NewsAPI
response = requests.get(url, params=params)

# si la solicitud fue exitosa, procesa los resultados
if response.status_code == 200:
    # convierte la respuesta de la API en un objeto JSON
    results = response.json()["articles"]

    # muestra los titulares de las noticias encontradas
    for article in results:
        print(article["title"])
else:
    # si la solicitud fallo, muestra el codigo de estado y el mensaje de error
    print(f"Error {response.status_code}: {response.reason}")
