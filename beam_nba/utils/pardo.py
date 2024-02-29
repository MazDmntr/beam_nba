import os
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
        
        response = get(
            url,
            headers={
                "Authorization": os.getenv("TOKEN")
            })

        next_cursor = (
            response.json()
            .get("meta")
            .get("next_cursor")
        )
        
        if next_cursor:
            try:                
                logging.info(f"Pagina retornou o status code: {response.status_code}")
                
                if response.status_code == 200: 
                    for player in response.json().get("data"):
                        yield player
            except Exception as e:
                logging.error(f"Erro na requisição: {e}")
