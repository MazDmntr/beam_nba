import logging
from apache_beam import DoFn
from requests import get

logging.basicConfig(
    level=logging.INFO, 
    filename="balls_dont_lie.log", 
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

class BallsDontLie(DoFn): 
    def process(self, element):    
        url = element.get("url")
        
        response = get(url)
        
        total_pages = (
            response.json()
            .get("meta")
            .get("total_pages")
        )
        
        for i in range(2, total_pages+1):
            try:
                response = get(url + "?page=" + str(i))
                
                logging.info(f"Pagina {i} retornou o status code: {response.status_code}")
                
                if response.status_code == 200: 
                    for player in response.json().get("data"):
                        yield player
            except Exception as e:
                logging.error(f"Erro na requisição: {e}")
