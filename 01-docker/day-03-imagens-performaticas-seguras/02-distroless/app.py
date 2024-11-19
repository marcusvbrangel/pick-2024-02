import requests
from loguru import logger # type: ignore

def main():

    logger.info("Iniciando a aplicação.\n")

    url = "https://jsonplaceholder.typicode.com/posts/1"

    logger.info(f"Fazendo uma requisição GET para {url} \n")

    try:
        response = requests.get(url)

        response.raise_for_status()

        postagem = response.json()

        logger.info(f"Postagem recebida: \n")
        
        logger.info(f"{postagem} \n")

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao fazer a requisição: {e} \n")

    logger.info("Finalizando a aplicação.\n")

if __name__ == "__main__":
    main()


# pip uninstall requests loguru

# pip install -r requirements.txt
#     Successfully installed loguru-0.7.2 requests-2.32.3

# python app.py
