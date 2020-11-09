import urequests as requests
import ujson 
import network
import time

#função pegar prev do tempo
def prev_temp():
        while True: 
            with open('config.json', 'r') as config_file:
                dados = ujson.load(config_file)

            cidade = dados['cidade']
            api_key = dados['API_Key']
            cidade_v = cidade.replace(" ", "%20")
            link = "http://api.weatherapi.com/v1/forecast.json?key="+ api_key + "&q=" + cidade_v +"&days=1"
            print (link)
            res = requests.get(url= link)
            dado = res.json()
            with open('clima_t.json', 'w') as clima:
                ujson.dump(dado,clima)
            clima.close()
            print("clima atualizado")
            time.sleep(600)




